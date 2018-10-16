# Once you’ve written tests, run them using the test command of your project’s manage.py utility: $ ./manage.py test
# Test discovery is based on the unittest module’s built-in test discovery. 
# By default, this will discover tests in any file named “test*.py” under the current working directory.

from django.test import TestCase
from artwork_image_processor.models import Image

# Create your tests here.
#    def test_whatever_list_view(self):
#        w = self.create_whateve:qr()
#        url = reverse("whatever.views.whatever")
#        resp = self.client.get(url)
#
#        self.assertEqual(resp.status_code, 200)
#        self.assertIn(w.title, resp.content)

# to test our document model
class ModelTestCase(TestCase):
		
	def test_image_description(self):
		img = Image(description="test create desc")
		self.assertEqual("test create desc", img.description)



