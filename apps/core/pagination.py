from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ('count', self.page.paginator.count),
                    ('next', self.get_next_link()),
                    ('previous', self.get_previous_link()),
                    ('last_page_number', self.page.paginator.num_pages),
                    ('results', data),
                ]
            )
        )
