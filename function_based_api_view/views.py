import re
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET','POST'])
def StudentView(request):
    if request.method == "GET":
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            


@api_view(['PUT','DELETE'])
def StudentViewUD(request,id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response("id not found")

    if request.method == "PUT":
        data = request.data
        serializer = StudentSerializer(student,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":'Data Updated'})
        else:
            return Response(serializer.errors)

    elif request.method == "DELETE":
        Student.objects.get(id=id).delete()
        return Response({"msg":'Data Deleted'})
           