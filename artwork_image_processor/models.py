from django.db import models

# Create your models here.

# this model is used to access the uploaded image from the user
# currently goes to site > static > media > tmp
# TODO: perhaps change 'tmp' to 'images'?
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='tmp/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # for string representation
    def __str__(self):
        return self.description