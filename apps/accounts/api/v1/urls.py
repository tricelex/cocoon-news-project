from django.urls import path

from apps.accounts.api.v1.views import AuthorAPIView

app_name = "authors_api"

urlpatterns = [
    path('', AuthorAPIView.as_view(), name='authors_list'),
]
