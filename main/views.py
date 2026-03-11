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

    out = io.StringIO()
    results = []
    
    try:
        # 1. Migrate
        call_command('migrate', no_input=True, stdout=out)
        results.append("✅ Migration: SUCCESS")
        
        # 2. Collectstatic
        call_command('collectstatic', no_input=True, interactive=False, clear=True, stdout=out)
        results.append("✅ Collectstatic: SUCCESS")
        
        # 3. List the logs
        log_output = out.getvalue()
        
        return HttpResponse(f"<h1>Deployment Setup Results</h1><pre>{'<br>'.join(results)}</pre><h2>Logs:</h2><pre>{log_output}</pre>")
    except Exception as e:
        return HttpResponse(f"<h1>Setup Failed</h1><pre>{str(e)}</pre>")
