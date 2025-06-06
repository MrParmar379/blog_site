from rest_framework import serializers
from .models import BlogsTable, BlogType

class BlogTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogType
        fields = ['type_id', 'type_title']

class BlogSerializer(serializers.ModelSerializer):
    blog_type = BlogTypeSerializer(read_only=True)
    blog_type_id = serializers.PrimaryKeyRelatedField(
        queryset=BlogType.objects.all(), source='blog_type'
    )

    class Meta:
        model = BlogsTable
        fields = ['blog_id', 'content', 'blog_type', 'blog_type_id']
