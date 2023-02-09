from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.accounts.models import Author, User


class AuthorAPIViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testauthor')
        Author.objects.create(user=user, name='Test', surname='Author', job_description='Test Job')
        cls.test_user = User.objects.create_user(username='testuser', password='secret')

    def setUp(self):
        self.client = APIClient()

    def test_view_url_exists_with_authentication(self):
        self.client.force_authenticate(user=self.test_user)
        response = self.client.get(reverse('accounts_api:authors_list'))
        assert response.status_code == status.HTTP_200_OK
        self.client.force_authenticate(user=None)

    def test_view_uses_correct_serializer(self):
        self.client.force_authenticate(user=self.test_user)
        response = self.client.get(reverse('accounts_api:authors_list'))
        self.assertEqual(response.data['results'][0]['name'], 'Test')
        self.client.force_authenticate(user=None)

    def test_view_returns_pagination_class(self):
        self.client.force_authenticate(user=self.test_user)
        response = self.client.get(reverse('accounts_api:authors_list'))
        self.assertIn('count', response.data)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.client.force_authenticate(user=None)

    def test_view_url_exists_no_authentication(self):
        response = self.client.get(reverse('accounts_api:authors_list'))
        assert response.status_code == status.HTTP_403_FORBIDDEN
