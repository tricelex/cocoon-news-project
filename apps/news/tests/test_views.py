from django.test import RequestFactory, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.models import Author, User
from apps.news.models import Article, Category


class ArticlesAPIViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = APIClient()

        self.user = User.objects.create_user(username='testuser', password='secret')
        self.author = Author.objects.create(
            user=self.user, name='John', surname='Doe', job_description='Software Engineer'
        )

        self.category = Category.objects.create(name='Test Category')
        self.article = Article.objects.create(
            title='Test Article',
            summary='Test Summary',
            content='Test Content',
            is_published=True,
            category=self.category,
            author=self.author,
        )
        self.client.force_authenticate(user=self.user)

    def test_get_articles(self):
        response = self.client.get(reverse('news_api:articles_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Article')


class CategoriesAPIViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = APIClient()

        self.user = User.objects.create_user(username='testuser', password='secretpassword')
        self.client.force_authenticate(user=self.user)

        self.category = Category.objects.create(name='Test Category')

    def test_get_categories(self):
        response = self.client.get(reverse('news_api:category_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Test Category')
