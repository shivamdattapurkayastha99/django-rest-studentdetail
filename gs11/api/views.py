# Viewsets  
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import viewsets
# from rest_framework.response import Response 
# class StudentViewset(viewsets.ViewSet):
#     def List(self, request):
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)
#     def retrieve(self, request,pk=None):
#         id=pk
#         if id is not None:
#             stu=Student.objects.get(pk=id)
#             serializer=StudentSerializer(stu)
#             return Response(serializer.data)
#     def create(self, request):
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'})
#         return Response(serializer.errors)
#     def update(self, request,pk):
#         id=pk
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data updated'})
#         return Response(serializer.errors)
#     def destroy(self, request,pk):
#         id=pk
#         stu=Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data deleted'})
# ========================================================
# Model ViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer