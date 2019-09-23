from django.urls import reverse
#from django.core.urlresolves import reverse(for old version)
from django.test import TestCase


# Create your tests here.

class HomeTests(TestCase):
 def test_home_view_status_code(self):
  url = reverse('home')
  response = self.client.get(url)
  self.assertEquals(response.status_code, 200)
 
