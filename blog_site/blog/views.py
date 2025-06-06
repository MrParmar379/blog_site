from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import BlogsTable
from .serializers import BlogSerializer
from django.http import JsonResponse

class BlogsTableAPIView(APIView):
    def post(self, request):
        try:
            serializer = BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': str(e)},"not creaed", status=status.HTTP_400_BAD_REQUEST)
        

        
    def get (self, request, pk=None):
        if pk is not None:
            try:
                blog = BlogsTable.objects.get(pk=pk)
                serializer = BlogSerializer(blog)
                return Response(serializer.data)
            except BlogsTable.DoesNotExist:
                return JsonResponse({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND) 
                
        blogs = BlogsTable.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk=None):
        try:
            blog = BlogsTable.objects.get(pk=pk)
        except BlogsTable.DoesNotExist:
            return JsonResponse({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND) 
        serializer = BlogSerializer(blog, data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse({'message': 'Blog not Update'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk=None):
        try:
            blog = BlogsTable.objects.get(pk=pk)
        except BlogsTable.DoesNotExist:
            return JsonResponse({'message': ' not found'}, status=status.HTTP_404_NOT_FOUND) 
        blog.delete()
        return JsonResponse({'message': ' Deleted'}, status=status.HTTP_404_NOT_FOUND)
    

    
 
