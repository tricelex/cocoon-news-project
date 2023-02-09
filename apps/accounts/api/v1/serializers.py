from rest_framework import serializers

from apps.accounts.models import Author


class AuthorSerializer(serializers.ModelSerializer[Author]):
    class Meta:
        model = Author
        fields = '__all__'
