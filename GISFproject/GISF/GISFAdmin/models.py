from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=500)

    class Meta:
        db_table = 'Users'


