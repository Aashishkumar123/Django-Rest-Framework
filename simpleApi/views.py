from django.http.response import JsonResponse
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import io
# Create your views here.


@csrf_exempt
def CreateAPI(request):
    if request.method == "POST":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg = {'success':'data created'}
        return JsonResponse(msg,safe=False)

def ReadAPI(request):
    if request.method == "GET":
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def UpdateAPI(request,pk):
    if request.method == "PUT":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        id = Student.objects.get(id=pk)
        serializer = StudentSerializer(id,data)
        if serializer.is_valid():
            serializer.save()
            msg = {'success':'data updated'}
        return JsonResponse(msg,safe=False)

@csrf_exempt
def DeleteAPI(request,pk):
    if request.method == "DELETE":
        Student.objects.get(id=pk).delete()
        msg = {'success':'data deleted'}
        return JsonResponse(msg,safe=False)
    return JsonResponse('data delete',safe=False)






    

    