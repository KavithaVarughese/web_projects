from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html'), name='main'),
]