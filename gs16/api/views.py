from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from api.models import Student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # =====================================
    # filter by current user
    # def get_queryset(self):
    #     user=self.request.user
    #     return Student.objects.filter(passby=user)
    # =========================================
    # filter using django filter backend
    # filter_backends=[DjangoFilterBackend]
    # filterset_fields=['city']
    # ========================================
    # Search filter
    # filter_backends=[SearchFilter]
    # search_fields=['city','name']
    # search_fields=['^name']
    # =========================================
    # Ordering Filter
    filter_backends=[OrderingFilter]
    ordering_fields=['name']
    
