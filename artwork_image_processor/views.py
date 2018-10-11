# settings import not used at this time
#from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from artwork_image_processor.models import Document
from artwork_image_processor.forms import DocumentForm

from style import run_style_transfer

# Create your views here.

# our current default home page
def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save('tmp/'+myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

# this model form upload is being used for the style transfer
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # the uploaded image is passed to the style transfer method
            run_style_transfer(form.save())
            # returns to transformed image result page
            return redirect('artwork_image_processor.views.image')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

# result transformed image result page
def image(request):
    return render(request, 'image.html', {'image': image })

# not currently being used
def index(request):
    return HttpResponse("Hello, world. You're at the aip index.")