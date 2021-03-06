from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.gallery_url = reverse('gallery')

    def test_item_gallery(self):
        response = self.client.get(self.gallery_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/gallery.html')


