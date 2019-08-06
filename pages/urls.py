from django.urls import path

from .views import HomePageView, AboutPageView
from django.views.generic import TemplateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('homepage/gokuvscooler', TemplateView.as_view(template_name='pages/gokuvscooler.html'), name='gokuvscooler'),
    path('homepage/gokuvsyakon', TemplateView.as_view(template_name='pages/gokuvsyakon.html'), name="gokuvsyakon"),
]
