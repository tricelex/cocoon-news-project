import uuid

from ckeditor.fields import RichTextField
from django.db import models

from apps.accounts.models import Author
from apps.core.base_model import BaseAbstractModel


class Category(BaseAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(BaseAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=100)
    summary = models.TextField()
    content = RichTextField()

    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False)

    def get_author_name(self):
        return self.author.name

    def get_category_name(self):
        return self.category.name

    def __str__(self):
        return self.title
