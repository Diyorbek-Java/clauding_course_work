from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('organizations/', TemplateView.as_view(template_name='organizations.html'), name='organizations'),
    path('departments/', TemplateView.as_view(template_name='departments.html'), name='departments'),
    path('job-positions/', TemplateView.as_view(template_name='job_positions.html'), name='job-positions'),
]
