from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('uploads/simple/', views.simple_upload, name='simple_upload'),
    path('uploads/form/', views.model_form_upload, name='model_form_upload'),
]
