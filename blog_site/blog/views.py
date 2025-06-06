from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import BlogsTable
from .serializers import BlogSerializer

class BlogsTableAPIView(APIView):
    def get(self, request, pk=None):
        # if pk is not None:
        #     blog = get_object_or_404(BlogsTable, pk=pk)
        #     serializer = BlogSerializer(blog)
        #     return Response(serializer.data)
        blogs = BlogsTable.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        blog = get_object_or_404(BlogsTable, pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = get_object_or_404(BlogsTable, pk=pk)
        blog.delete()
        return Response({'message': 'Blog deleted '}, status=status.HTTP_204_NO_CONTENT)
