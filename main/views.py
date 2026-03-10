from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.template.loader import get_template
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
    if not HAS_XHTML2PDF:
        return HttpResponse("PDF generation not available.", status=500)

    template = get_template('resume_template.html')
    context = {
        'skills': Skill.objects.all(),
        'projects': Project.objects.filter(featured=True),
    }
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Tanvir_Ahmed_Joy_Resume.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response


def blog_list(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'blog_detail.html', {'post': post})
