from rest_framework import serializers

from apps.news.models import Article, Category


class ArticleSerializer(serializers.ModelSerializer[Article]):
    author = serializers.CharField(source='get_author_name', read_only=True)
    category = serializers.CharField(source='get_category_name', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer[Category]):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer[Category]):
    class Meta:
        model = Category
        fields = '__all__'
