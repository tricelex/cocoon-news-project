from django_filters import FilterSet, OrderingFilter

from apps.news.models import Article


class ArticlesFilter(FilterSet):
    created_datetime = OrderingFilter(fields=['created_datetime'])

    class Meta:
        model = Article
        fields = ['author', 'category', 'created_datetime']
