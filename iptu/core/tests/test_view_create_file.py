from django.test import TestCase
from django.shortcuts import resolve_url as r


class ViewCreateFileTest(TestCase):

    def setUp(self):
        self.response = self.client.get(r('create_file'))

    def test_get(self):
        """GET /create_file/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """"Must use create_file.html"""
        self.assertTemplateUsed(self.response, 'create_file.html')
