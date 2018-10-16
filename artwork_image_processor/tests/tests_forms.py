# Once you’ve written tests, run them using the test command of your project’s manage.py utility: $ ./manage.py test
# Test discovery is based on the unittest module’s built-in test discovery. 
# By default, this will discover tests in any file named “test*.py” under the current working directory.

import os
from django.conf import settings

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from artwork_image_processor.forms import *
from artwork_image_processor.models import Image

# Create your tests here.
#    def test_whatever_list_view(self):
#        w = self.create_whateve:qr()
#        url = reverse("whatever.views.whatever")
#        resp = self.client.get(url)
#
#        self.assertEqual(resp.status_code, 200)
#        self.assertIn(w.title, resp.content)

# Test image upload
class FormsTestCase(TestCase):
    
    def test_image_upload_form(self):
        
        # Load in test image as file object
        img = SimpleUploadedFile('static/unit_testing/0100.png', 
                content=open(os.path.join(settings.MEDIA_ROOT, 'static/unit_testing/0100.png'), 'rb').read(), 
                content_type="image/png")

        # Create test data for form
        form_data = {'description': 'something2134'}
        file_data = {'imageFile': img}
        form = ImageForm(form_data, file_data)

        # Assert form is valid
        self.assertTrue(form.is_valid())
       
