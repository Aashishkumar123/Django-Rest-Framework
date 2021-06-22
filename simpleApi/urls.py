from django.urls import path
from .import views


urlpatterns = [
    path('Api/read/',views.ReadAPI),
    path('Api/create/',views.CreateAPI),
    path('Api/update/<int:pk>/',views.UpdateAPI),
    path('Api/delete/<int:pk>',views.DeleteAPI),
]
