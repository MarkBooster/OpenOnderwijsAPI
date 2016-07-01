from collections import OrderedDict
from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    page_query_param = 'pageNumber'
    page_size = 10
    page_size_query_param = 'pageSize'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('meta', OrderedDict([
                ('next', self.get_next_link()),
                ('prev', self.get_previous_link()),
                ('totalPages', self.page.paginator.num_pages),
                ('totalItems', self.page.paginator.count),
            ])),
            ('data', data)
        ]))
