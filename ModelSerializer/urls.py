from django.urls import path
from .import views


urlpatterns = [
    path('Api/read1/',views.ReadAPI),
    path('Api/create1/',views.CreateAPI),
    path('Api/update1/<int:pk>/',views.UpdateAPI),
    path('Api/delete1/<int:pk>',views.DeleteAPI),
]
