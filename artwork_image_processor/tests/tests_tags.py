from django.test import TestCase
from django.core.files import File
from artwork_image_processor.models import Image
from artwork_image_processor.tags import add_photo_tags

# Create your tests here.
class StyleTestCase(TestCase):
    
    def test_add_photo_tags(self):
        image = Image(description="test create desc", imageFile='static/unit_testing/0100.png')
        self.assertTrue(add_photo_tags(image))
