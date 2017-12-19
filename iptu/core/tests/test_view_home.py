from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """"Must be use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_url_create_db(self):
        expected = f'href="{r("create_file")}"'
        self.assertContains(self.response, expected)
