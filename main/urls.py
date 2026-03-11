from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_submit, name='contact_submit'),
    path('download-resume/', views.download_resume, name='download_resume'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('deploy-setup/', views.deploy_setup, name='deploy_setup'),
]
