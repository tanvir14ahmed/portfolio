from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.template.loader import get_template
from django.core.management import call_command
import io
from .models import Skill, Project, Testimonial, BlogPost, ContactMessage
from .forms import ContactForm

try:
    from xhtml2pdf import pisa
    HAS_XHTML2PDF = True
except ImportError:
    HAS_XHTML2PDF = False


def index(request):
    skills_by_category = {}
    for skill in Skill.objects.all():
        cat = skill.get_category_display()
        skills_by_category.setdefault(cat, []).append(skill)

    context = {
        'skills_by_category': skills_by_category,
        'projects': Project.objects.filter(featured=True),
        'all_projects': Project.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'blog_posts': BlogPost.objects.filter(published=True)[:3],
        'contact_form': ContactForm(),
    }
    return render(request, 'index.html', context)


@require_POST
def contact_submit(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Thank you! Your message has been sent.'})
    else:
        errors = {field: error[0] for field, error in form.errors.items()}
        return JsonResponse({'success': False, 'errors': errors}, status=400)


def download_resume(request):
    import os
    from django.conf import settings
    file_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'files', 'resume.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponse("Resume not found.", status=404)


def blog_list(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'blog_detail.html', {'post': post})

def deploy_setup(request):
    """
    A view to run migrations and collectstatic without terminal access.
    URL: /deploy-setup/?key=tanvir_secure_setup
    """
    if request.GET.get('key') != 'tanvir_secure_setup':
        return HttpResponse("Unauthorized", status=403)

    import os
    import io
    from django.core.management import call_command
    from django.conf import settings
    
    out = io.StringIO()
    results = []
    
    try:
        # 1. Fix Permissions on DB and folder
        db_path = settings.DATABASES['default']['NAME']
        db_dir = os.path.dirname(db_path)
        
        try:
            os.chmod(db_dir, 0o775)
            results.append(f"✅ Directory permissions set to 775: {db_dir}")
            if os.path.exists(db_path):
                os.chmod(db_path, 0o666)
                results.append(f"✅ Database permissions set to 666: {db_path}")
        except Exception as perm_err:
            results.append(f"⚠️ Permission fix warning: {perm_err}")

        # 2. Migrate
        call_command('migrate', no_input=True, stdout=out)
        results.append("✅ Migration: SUCCESS")
        
        # 3. Collectstatic
        call_command('collectstatic', no_input=True, interactive=False, clear=True, stdout=out)
        results.append("✅ Collectstatic: SUCCESS")
        
        # 4. Show results
        log_output = out.getvalue()
        
        return HttpResponse(f"""
            <html><body style='font-family: monospace; background: #1a1a1a; color: #00ff00; padding: 20px;'>
            <h1>Deployment Setup Results</h1>
            <ul style='list-style: none; padding: 0;'>{''.join([f'<li>{r}</li>' for r in results])}</ul>
            <hr>
            <h2>Full Logs:</h2>
            <pre style='background: #000; padding: 15px; border-radius: 5px;'>{log_output}</pre>
            <p><a href='/' style='color: cyan;'>Go to Home</a> | <a href='/admin/' style='color: cyan;'>Go to Admin</a></p>
            </body></html>
        """)
    except Exception as e:
        import traceback
        return HttpResponse(f"<h1>Setup Failed</h1><pre>{traceback.format_exc()}</pre>")
