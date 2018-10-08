from django import forms
from artwork_image_processor.models import Image

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'image', )
