from django.test import TestCase

from apps.accounts.models import Author, User
from apps.news.api.v1.serializers import ArticleSerializer, CategorySerializer
from apps.news.models import Article, Category


class ArticleSerializerTestCase(TestCase):
    def setUp(self):
        # Create some test data
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.author = Author.objects.create(
            user=self.user, name='John', surname='Doe', job_description='Software Engineer'
        )
        self.category = Category.objects.create(
            name='Technology',
        )
        self.article = Article.objects.create(
            title='Test Article',
            summary='Test summary',
            content='<p>Test content</p>',
            is_published=True,
            published_date='2022-01-01T00:00:00Z',
            category=self.category,
            author=self.author,
        )

    def test_serializer_with_valid_data(self):
        serializer = ArticleSerializer(self.article)
        self.assertEqual(
            serializer.data,
            {
                'id': str(self.article.id),
                'title': 'Test Article',
                'summary': 'Test summary',
                'content': '<p>Test content</p>',
                'is_published': True,
                'published_date': '2022-01-01T00:00:00Z',
                'category': 'Technology',
                'author': 'John',
                'created_datetime': serializer.data['created_datetime'],
                'updated_datetime': serializer.data['updated_datetime'],
            },
        )


class CategorySerializerTestCase(TestCase):
    def setUp(self):
        # Create some test data
        self.category = Category.objects.create(
            name='Technology',
        )

    def test_serializer_with_valid_data(self):
        serializer = CategorySerializer(self.category)
        self.assertEqual(
            serializer.data,
            {
                'id': str(self.category.id),
                'name': 'Technology',
                'created_datetime': serializer.data['created_datetime'],
                'updated_datetime': serializer.data['updated_datetime'],
            },
        )
