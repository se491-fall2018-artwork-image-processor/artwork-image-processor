# =============================================================================
#          >>>  PLACEHOLDER METHOD TO TRANSFORM AN IMAGE    <<<
#          >>>      This version transforms an image        <<<
#          >>>      WITHOUT using Tensorflow methods        <<<
# https://www.pyimagesearch.com/2018/08/27/neural-style-transfer-with-opencv/
# =============================================================================

import os
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from artwork_image_processor.models import Image

import PIL.Image
import imutils
import cv2
import numpy as np  

from scipy.misc import toimage

from artwork_image_processor_site.settings import BASE_DIR

model_path = os.path.join(BASE_DIR, 'media', 'static', 'style_transfer', 'models',
'eccv16', 'la_muse.t7')

def run_style_transfer(img):

    # build the model
  net = cv2.dnn.readNetFromTorch(model_path)

  # open the image and transform to numpy array (preprocessing)
  PIL_image = PIL.Image.open(img.imageFile).convert('RGB')
  PIL_image = np.array(PIL_image)
  image = PIL_image[:, :, ::-1].copy()

  # resize for neural net
  image = imutils.resize(image, width=600)
  (h, w) = image.shape[:2]

  # run through neural net
  blob = cv2.dnn.blobFromImage(image, 1.0, (w,h), 
  (103.939, 116.779, 123.680), swapRB=False, crop=False)
  net.setInput(blob)
  output = net.forward()

  # transform output (deprocessing)
  output = output.reshape((3, output.shape[2], output.shape[3]))
  output[0] += 103.939
  output[1] += 116.779
  output[2] += 123.680
  output /= 255.0
  output = output.transpose(1, 2, 0)

  # Create a file-like object to write styled image data (image data previously created
  # using PIL, and stored in variable 'generatedImage', now using scipy toimage)
  generatedImage = toimage(output)

  generatedImage_io = BytesIO()
  generatedImage.save(generatedImage_io, format='PNG')

  # Create a new Django file-like object to be used in models as ImageField using InMemoryUploadedFile
  generatedImageFile = InMemoryUploadedFile(generatedImage_io, None, os.path.splitext(img.imageFile.name)[0] + '_styled.png', 'image/png', generatedImage_io.getbuffer().nbytes, None)

  # Create a new Image model object to hold styled image
  generatedImageModel = Image()
  generatedImageModel.description = img.description
  generatedImageModel.tags = img.tags
  generatedImageModel.imageFile = generatedImageFile
  generatedImageModel.save()
  
  return generatedImageModel
   
