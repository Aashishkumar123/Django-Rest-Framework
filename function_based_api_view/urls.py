from django.urls import path
from .import views

urlpatterns = [
    path('student-data/',views.StudentView,name="stuAPI"),
    path('student-data/<int:id>/',views.StudentViewUD,name="stuAPIUD"),
]
