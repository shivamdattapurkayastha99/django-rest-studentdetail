from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
# class MyPageNumberPagination(PageNumberPagination):
#     page_size=2
# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit=2
class MyCursorPagination(CursorPagination):
    page_size=2
    ordering='name'