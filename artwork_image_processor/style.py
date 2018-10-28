# =============================================================================
#         PLACEHOLDER METHODS TO TRANSFORM AN IMAGE
#           This version only does grayscale
# =============================================================================

import os
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from artwork_image_processor.models import Image
import PIL.Image

def run_style_transfer(img):
  image = PIL.Image.open(img.imageFile)
  generatedImage = image.convert(mode='L')

  # Create a file-like object to write styled image data (image data previously created
  # using PIL, and stored in variable 'generatedImage')
  generatedImage_io = BytesIO()
  generatedImage.save(generatedImage_io, format='PNG')

  # Create a new Django file-like object to be used in models as ImageField using InMemoryUploadedFile
  generatedImageFile = InMemoryUploadedFile(generatedImage_io, None, os.path.splitext(img.imageFile.name)[0] + '_styled.png', 'image/png', generatedImage_io.getbuffer().nbytes, None)

  # Create a new Image model object to hold styled image
  generatedImageModel = Image()
  generatedImageModel.description = img.description
  generatedImageModel.imageFile = generatedImageFile
  generatedImageModel.save()
  return generatedImageModel
   
