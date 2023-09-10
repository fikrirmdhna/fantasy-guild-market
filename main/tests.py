from django.test import TestCase, Client

# Create your tests here.
class appTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main')
        self.assertEqual(response.status_code,200)