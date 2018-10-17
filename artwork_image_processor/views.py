# settings import not used at this time
#from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from artwork_image_processor.models import Image
from artwork_image_processor.forms import ImageForm

from artwork_image_processor.style import run_style_transfer

# Create your views here.

# our current default home page
def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', { 'images': images })

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save('static/'+myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

# this model form upload is being used for the style transfer
def model_form_upload(request):
    if request.method == 'POST':
        imageForm = ImageForm(request.POST, request.FILES)
        if imageForm.is_valid():
           
            # the uploaded image is passed to the style transfer method
            uploadedImage = imageForm.save()
            styledImage = run_style_transfer(uploadedImage)
             
            content = {
                'imageForm': imageForm,
                'image': styledImage, 
            }
            return render(request, 'model_form_upload.html', content)
    else:
        imageForm = ImageForm() 
    return render(request, 'model_form_upload.html', {
        'imageForm': imageForm,  
    })

# result transformed image result page
def image(request):
    return render(request, 'image.html', {'image': image })

# not currently being used
def index(request):
    return HttpResponse("Hello, world. You're at the aip index.")
