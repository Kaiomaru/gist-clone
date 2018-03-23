from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from api.models import Gist
from api.views import GistsAPIView

User = get_user_model()

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

class GistAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='test_user')
        user_obj.set_password('randompw')
        user_obj.save()
        gist = Gist.objects.create(
                user=user_obj,
                title='Test Title',
                text='Some Content'
            )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_gist(self):
        gist_count = Gist.objects.count()
        self.assertEqual(gist_count, 1)

    def test_unauthorized_get_gist_list(self):
        data = {}
        url = reverse('gists-api-view')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_get_one_gist(self):
        data = {}
        url = Gist.objects.first().get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_post_gist(self):
        data = {'title': 'Some Title', 'text': 'Some Text'}
        url = reverse('gists-api-view')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_unauthorized_delete_gist(self):
        data = {}
        url = Gist.objects.first().get_api_url()
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        gist_count = Gist.objects.count()
        self.assertEqual(gist_count, 1)

    def test_authorized_get_gist_list(self):
        data = {}
        url = reverse('gists-api-view')
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_response = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response)
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authorized_get_one_gist(self):
        data = {}
        url = Gist.objects.first().get_api_url()
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_response = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response)
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authorized_post_gist(self):
        data = {'title': 'Some Title', 'text': 'Some Text'}
        url = reverse('gists-api-view')
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_response = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_authorized_delete_gist(self):
        data = {}
        url = Gist.objects.first().get_api_url()
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_response = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response)
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        gist_count = Gist.objects.count()
        self.assertEqual(gist_count, 0)

    def test_get_gist_created_by_another_user(self):
        first_user = User.objects.first()
        second_user = User(username='test_user2')
        second_user.set_password('randompw')
        second_user.save()

        gist = Gist.objects.create(
                user=first_user,
                title='Test Title',
                text='Some Content'
            )
        url = gist.get_api_url()
        payload = payload_handler(second_user)
        token_response = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response)
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

    def test_same_title_adding(self):
        user_obj = User.objects.first()
        data = {
            'title': 'Same title',
            'text': 'Some text'
        }
        data = {'title': 'Some Title', 'text': 'Some Text'}
        url = reverse('gists-api-view')
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_response = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response)
        response = self.client.post(url, data, format='json')
        response = self.client.post(url, data, format='json') 
        gist_count = Gist.objects.count()
        self.assertEqual(gist_count, 2) #1 in setUp
        


