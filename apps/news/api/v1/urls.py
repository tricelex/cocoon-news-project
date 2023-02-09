from django.urls import path

from apps.news.api.v1.views import ArticlesAPIView, CategoriesAPIView

urlpatterns = [
    path('articles/', ArticlesAPIView.as_view(), name='articles_list'),
    path('category/', CategoriesAPIView.as_view(), name='category_list'),
]
