import pytest
from rest_framework.exceptions import ErrorDetail

from apps.accounts.api.v1.serializers import AuthorSerializer
from apps.accounts.models import Author, User


@pytest.mark.django_db
class TestAuthorSerializer:
    def setup(self):
        self.user = User.objects.create(username='testauthor')
        self.author = Author.objects.create(user=self.user, name='Test', surname='Author', job_description='Test Job')

    def test_serialize_author(self):
        serializer = AuthorSerializer(self.author)
        assert serializer.data == {
            'id': str(self.author.id),
            'user': self.author.user.id,
            'name': 'Test',
            'surname': 'Author',
            'job_description': 'Test Job',
            'created_datetime': serializer.data['created_datetime'],
            'updated_datetime': serializer.data['updated_datetime'],
        }

    def test_validate_author(self):
        self.user_2 = User.objects.create(username='testauthor2')

        data = {'user': '', 'name': '', 'surname': '', 'job_description': ''}
        serializer = AuthorSerializer(data=data)
        assert not serializer.is_valid()
        assert serializer.errors == {'user': [ErrorDetail(string='This field may not be null.', code='null')]}
