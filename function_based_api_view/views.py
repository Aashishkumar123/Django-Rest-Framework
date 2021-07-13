from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET'])
def StudentView(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    return Response(serializer.data)
