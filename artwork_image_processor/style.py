# =============================================================================
#         PLACEHOLDER METHODS TO TRANSFORM AN IMAGE
#           This version simply changes the image to grayscale
# =============================================================================

import os
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image as PIL_Image
from artwork_image_processor.models import Image


def run_style_transfer(img):
    pil_image = PIL_Image.open(img.imageFile)
    generatedImage = pil_image.convert(mode='L') 
   
    # Create a file-like object to write styled image data (image data previously created
    # using PIL, and stored in variable 'generatedImage')
    generatedImage_io = BytesIO()
    generatedImage.save(generatedImage_io, format='PNG')

    # Create a new Django file-like object to be used in models as ImageField using InMemoryUploadedFile
    generatedImageFile = InMemoryUploadedFile(generatedImage_io, None, os.path.splitext(img.imageFile.name)[0] + '_styled.png', 'image/png', generatedImage_io.getbuffer().nbytes, None)
    #generatedImageFile.name = img.imageFile.name + '_styled.PNG'

    # Create a new Image model object to hold styled image
    generatedImageModel = Image()
    generatedImageModel.description = img.description
    generatedImageModel.imageFile = generatedImageFile
    generatedImageModel.save()

    return generatedImageModel
    
