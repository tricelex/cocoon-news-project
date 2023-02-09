import uuid

import pytest
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.test import TestCase

from apps.accounts.models import Author, User


class UserModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='testuser')

    def test_user_uuid_field(self):
        user = User.objects.get(username='testuser')
        assert isinstance(user.user_uuid, uuid.UUID)

    def test_str_method(self):
        user = User.objects.get(username='testuser')
        assert str(user) == f'testuser - {str(user.user_uuid)}'

    def test_get_full_name(self):
        user = User.objects.get(username='testuser')
        assert user.get_full_name() == ''


class AuthorModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testauthor')
        Author.objects.create(user=user, name='Test', surname='Author', job_description='Test Job')

    def test_author_id_field(self):
        author = Author.objects.get(name='Test')
        assert isinstance(author.id, uuid.UUID)

    def test_str_method(self):
        author = Author.objects.get(name='Test')
        assert str(author) == 'Test Author'

    def test_related_name(self):
        user = User.objects.get(username='testauthor')
        author = user.author
        assert author.name == 'Test'
