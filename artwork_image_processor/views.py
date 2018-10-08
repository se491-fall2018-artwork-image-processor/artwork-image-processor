from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from artwork_image_processor.models import Image
from artwork_image_processor.forms import ImageForm

# Create your views here.

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

def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('artwork_image_processor.views.home')
            content = {
                'form': form,
            }
            return render(request, 'model_form_upload.html', content)
    else:
        if 'form' not in locals():
            form = ImageForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

def index(request):
    return HttpResponse("Hello, world. You're at the aip index.")
