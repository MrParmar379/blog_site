from django.urls import path
from .views import UserTableAPIView

urlpatterns = [
    path('user/', UserTableAPIView.as_view()),               
    path('user/<int:pk>/', UserTableAPIView.as_view()),      
]
