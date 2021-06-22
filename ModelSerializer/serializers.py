from rest_framework import serializers
from .models import Student

class StudentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id','name','email']