from django.test import TestCase


class HomeViewTest(TestCase):

    def test_home_page(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get('/about/')

        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get('/contact/')

        self.assertEqual(response.status_code, 200)