from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# home, simple upload, model form upload, and transform result page views
# + media url to be able to click on the images through the browser
urlpatterns = [
    path('', views.home, name='artwork_image_processor.views.home'),
    path('uploads/simple/', views.simple_upload, name='artwork_image_processor.views.simple_upload'),
    path('uploads/form/', views.model_form_upload, name='artwork_image_processor.views.model_form_upload'),
    path('transform/image/', views.image, name='artwork_image_processor.views.image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 