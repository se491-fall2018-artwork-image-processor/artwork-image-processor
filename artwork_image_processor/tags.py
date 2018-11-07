# =============================================================================
#         Methods for interacting with the PhotoTagger API
# =============================================================================

# TODO: Parameterize the POST URL

from django.conf import settings
from artwork_image_processor.models import Image
import requests
import json

def add_photo_tags(imgModel):
   
    # Get Photo Tagger Classify API Endpoint URL from settings.py
    # Final value is default in case value is not set in settings.py
    PHOTOTAGGER_CLASSIFY_API_ENDPOINT = getattr(settings, "PHOTOTAGGER_CLASSIFY_API_ENDPOINT", "http://phototagger491.herokuapp.com/api/classify/") 

    # Open the image file for POST to API
    image = open(str(imgModel.imageFile.file), 'rb')

    # Create 'multipart/form-data' object
    # See requests module documentation for more info: 
    #    http://docs.python-requests.org/en/master/user/quickstart/?highlight=multipart#post-a-multipart-encoded-file
    files = {'file':(imgModel.imageFile.name, image)}

    # Create a post request to Photo-tagger API
    resp = requests.post(PHOTOTAGGER_CLASSIFY_API_ENDPOINT, files=files)

    # Parse json into python dictionary
    resp_json = json.loads(resp.text)

    # Extract list of tags from json, then convert list to string of comma-separated vals
    # Save string to image model "tags" field
    if resp_json['tags'] is not None:
      imgModel.tags = ', '.join(resp_json['tags'])
      imgModel.save()
    
    return imgModel
