from django import forms
from artwork_image_processor.models import Document

# this is the basic form upload
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

# this is the form upload we are using
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
