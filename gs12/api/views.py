
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .customPermissions import MyPermission
# Authentication-BasicAuthentication
# basic authentication allows any authenticated user be it staff,superuser or normal user to
# perform crud operations
# ============================
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     authentication_classes=[BasicAuthentication]
#     permission_classes=[IsAuthenticated]
# Basic Authentication and IsAdminUser
# ========================
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     authentication_classes=[BasicAuthentication]
#     # permission_classes=[AllowAny]
#     permission_classes=[IsAdminUser]
# Session Authentication
# ===========================
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     authentication_classes=[SessionAuthentication]
#     # permission_classes=[IsAuthenticated]
#     # permission_classes=[IsAuthenticatedOrReadOnly]
#     # permission_classes=[DjangoModelPermissions]
#     permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
# ========================
#Custom Permission class
# =========================== 
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[MyPermission]