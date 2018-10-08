# Once you’ve written tests, run them using the test command of your project’s manage.py utility: $ ./manage.py test
# Test discovery is based on the unittest module’s built-in test discovery. 
# By default, this will discover tests in any file named “test*.py” under the current working directory.

from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class ViewsTestCase(TestCase):
    
    def test_home_view(self):
        #w = self.create_whatever()
        url = reverse("artwork_image_processor.views.home")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        #self.assertIn(w.title, resp.content)

    def test_simple_upload_view(self):
        url = reverse("artwork_image_processor.views.simple_upload")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_model_form_upload_view(self):
        url = reverse("artwork_image_processor.views.model_form_upload")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

