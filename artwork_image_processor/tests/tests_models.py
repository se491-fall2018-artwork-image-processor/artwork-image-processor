# Once you’ve written tests, run them using the test command of your project’s manage.py utility: $ ./manage.py test
# Test discovery is based on the unittest module’s built-in test discovery. 
# By default, this will discover tests in any file named “test*.py” under the current working directory.

import os
from django.conf import settings
from django.test import TestCase
from artwork_image_processor.models import Image
from django.core.files.uploadedfile import SimpleUploadedFile

# Tests for our Image model
class ModelTestCase(TestCase):
        
        def test_image_tags(self):
            img = Image(tags="test create tags")
            self.assertEqual("test create tags", img.tags)
    
        def test_image_description(self):
            img = Image(description="test create desc")
            self.assertEqual("test create desc", img.description)

        def test_image_imageFile(self):
            
            # Load in test image as file object
            imgCompare = SimpleUploadedFile('static/unit_testing/0100.png',
                content=open(os.path.join(settings.MEDIA_ROOT, 'static/unit_testing/0100.png'), 'rb').read(),
                content_type="image/png")

            img = Image(imageFile='static/unit_testing/0100.png')
            self.assertIsNotNone(img.imageFile)
            self.assertEqual(img.imageFile.size, imgCompare.size)
