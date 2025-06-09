from django.db import models

class BlogType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_title = models.CharField(max_length=50)
    

    def __str__(self):
        return self.type_title

class BlogsTable(models.Model):
    blog_id = models.AutoField(primary_key=True)
    content = models.TextField()
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.content
