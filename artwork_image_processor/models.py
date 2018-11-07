import uuid
from django.db import models

# Create your models here.

# This model is used to access the uploaded image from the user
# Currently goes to media > uploaded_images
class Image(models.Model):
    description = models.CharField(max_length=255, blank=True)
    imageFile = models.ImageField(upload_to='image_uploads/')
    image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=500, blank=True)

    # for string representation
    def __str__(self):
        return self.description
