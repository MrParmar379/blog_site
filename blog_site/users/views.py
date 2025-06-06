from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.http import JsonResponse

class UserTableAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return JsonResponse({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND) 
                    
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': str(e)},"not creaed", status=status.HTTP_400_BAD_REQUEST) 
    

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND) 
        serializer = UserSerializer(user, data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse({'message': 'User not Update'}, status=status.HTTP_404_NOT_FOUND) 

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND) 
        user.delete()
        return JsonResponse({'message': 'User Deleted'}, status=status.HTTP_404_NOT_FOUND) 
