from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.template.loader import get_template
from .models import Skill, Project, Testimonial, BlogPost, ContactMessage
from .forms import ContactForm

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

def test_view(request):
    import os
    from django.db import connection
    from django.conf import settings
    
    db_status = "Unknown"
    try:
        connection.ensure_connection()
        db_status = "✅ Connected to Database!"
    except Exception as e:
        db_status = f"❌ DB ERROR: {str(e)}"
    
    db_file = settings.DATABASES['default']['NAME']
    db_exists = "✅ Exists" if os.path.exists(db_file) else "❌ MISSING"
    
    html = f"""
    <h1>Diagnostic Page</h1>
    <ul>
        <li><b>Server Status:</b> Running!</li>
        <li><b>Database Path:</b> {db_file}</li>
        <li><b>Database File:</b> {db_exists}</li>
        <li><b>Database Connection:</b> {db_status}</li>
    </ul>
    <p>Check <b>django_debug.log</b> in File Manager for details.</p>
    """
    return HttpResponse(html)
