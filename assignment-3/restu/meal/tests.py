from django.test import SimpleTestCase
from django.urls import reverse

from .views import MENU


class PageTests(SimpleTestCase):
    def test_landing_page_at_root_and_old_url(self):
        for url in ['/', '/meal/index/']:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'meal/index.html')
                self.assertContains(response, "<title>Home | King's Restora</title>", html=False)

    def test_menu_lists_every_category(self):
        response = self.client.get(reverse('meal'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['categories']), len(MENU['categories']))
        for item in MENU['categories']:
            self.assertContains(response, item['strCategory'])
            self.assertContains(response, reverse('meal_detail', args=[item['idCategory']]))

    def test_menu_also_served_at_meal_url(self):
        self.assertTemplateUsed(self.client.get('/meal/'), 'meal/meal.html')

    def test_menu_category_detail(self):
        response = self.client.get(reverse('meal_detail', args=[6]))
        self.assertContains(response, 'Pasta')
        self.assertContains(response, 'dried (pasta secca)')  # full description, not truncated

    def test_unknown_menu_category_returns_404(self):
        self.assertEqual(self.client.get(reverse('meal_detail', args=[99])).status_code, 404)

    def test_navbar_marks_current_page(self):
        response = self.client.get(reverse('meal'))
        self.assertContains(response, f'class="nav-link active" href="{reverse("meal")}"', html=False)
        self.assertContains(response, f'class="nav-link " href="{reverse("about_us")}"', html=False)
