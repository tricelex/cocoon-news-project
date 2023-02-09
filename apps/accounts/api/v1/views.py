from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.accounts.api.v1.serializers import AuthorSerializer
from apps.accounts.models import Author
from apps.core.pagination import CustomPagination
from apps.core.utils import GetObjectMixin


class AuthorAPIView(GetObjectMixin, ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = CustomPagination

    def get(self, request: Request) -> Response:

        page = self.paginate_queryset(self.get_queryset())
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
