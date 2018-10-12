from django.test import TestCase
from django.core.files import File
from artwork_image_processor.models import Document
from artwork_image_processor.style import run_style_transfer
# Create your tests here.
class StyleTestCase(TestCase):
    
    def test_run_style_transfer(self):
        doc = Document(description="test create desc", document='unit_testing/0100.png')
        self.assertTrue(run_style_transfer(doc))