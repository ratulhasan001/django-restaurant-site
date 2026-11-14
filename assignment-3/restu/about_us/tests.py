from django.test import SimpleTestCase
from django.urls import reverse


class AboutUsTests(SimpleTestCase):
    def test_about_page(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(reverse('about_us'), '/about_us/')
        self.assertContains(response, 'css/style.css')
        self.assertContains(response, reverse('meal'))
