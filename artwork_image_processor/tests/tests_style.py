from django.test import TestCase
from django.core.files import File
from artwork_image_processor.models import Image
from artwork_image_processor.style import run_style_transfer

# Create your tests here.
class StyleTestCase(TestCase):
    
    def test_run_style_transfer(self):
        image = Image(description="test create desc", imageFile='static/unit_testing/0100.png')
        self.assertTrue(run_style_transfer(image))
