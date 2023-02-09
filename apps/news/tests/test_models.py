import pytest
from django.test import TestCase

from apps.accounts.models import Author, User
from apps.news.models import Article, Category


@pytest.mark.django_db
class TestCategoryModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Sports")

    def test_category_name(self):
        assert self.category.name == "Sports"

    def test_str_representation(self):
        assert str(self.category) == "Sports"


@pytest.mark.django_db
class TestArticleModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.author = Author.objects.create(user=self.user, name='Test', surname='Author', job_description='Test Job')
        self.category = Category.objects.create(name="Sports")
        self.article = Article.objects.create(
            title="Test Article",
            summary="This is a test article.",
            content="<p>This is the content of the test article.</p>",
            author=self.author,
            category=self.category,
        )

    def test_article_title(self):
        assert self.article.title == "Test Article"

    def test_article_summary(self):
        assert self.article.summary == "This is a test article."

    def test_article_content(self):
        assert self.article.content == "<p>This is the content of the test article.</p>"

    def test_author_name(self):
        assert self.article.get_author_name() == "Test"

    def test_category_name(self):
        assert self.article.get_category_name() == "Sports"

    def test_str_representation(self):
        assert str(self.article) == "Test Article"
