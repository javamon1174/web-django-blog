from django.test import TestCase
from blog.views import  *
from django.test import Client
import datetime

client = Client()

class PostListTests(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def test_url_mapping_to_username(self):
        response = client.get('/1/') # http://host/1
        print(response.status_code)
        # self.assertTrue(response.status_code == 200)

    # def test_request_post_detail(self): # 하 빡치네
    #     print('-'*30+' test_request_post_detail '+'-'*30)
    #     response = client.get('/javamon/1')
    #     print(response.status_code)
