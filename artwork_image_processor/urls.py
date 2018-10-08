from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='artwork_image_processor.views.home'),
    path('uploads/simple/', views.simple_upload, name='artwork_image_processor.views.simple_upload'),
    path('uploads/form/', views.model_form_upload, name='artwork_image_processor.views.model_form_upload'),
]
