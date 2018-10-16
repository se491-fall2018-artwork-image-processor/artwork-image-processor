from django import forms
from artwork_image_processor.models import Image

# this is the basic form upload
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

# this is the form upload we are using
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'imageFile', )
