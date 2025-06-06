from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=50)
    user_bussiness = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name