from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.dashboard.views import (
    ArticleCreateUpdateView,
    ArticleListView,
    login_view,
    register_user,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles_list"),
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('articles/create/', ArticleCreateUpdateView.as_view(), name='article_create'),
    path('articles/<uuid:article_id>/update/', ArticleCreateUpdateView.as_view(), name='article_update'),
]
