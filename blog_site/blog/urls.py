from django.urls import path
from .views import BlogsTableAPIView

urlpatterns = [
    path('blogs/', BlogsTableAPIView.as_view()),               
    path('blogs/<int:pk>/', BlogsTableAPIView.as_view()),      
]
