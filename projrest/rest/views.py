from django.shortcuts import render
from .models import Student
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    
    return JsonResponse(serializer.data)
    # Queryset all students data  
def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    
    return JsonResponse(serializer.data,safe=False)


