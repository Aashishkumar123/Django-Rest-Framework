from django.urls import path
from .import views

urlpatterns = [
    path('student-data/',views.StudentView,name="stuAPI"),
]
