from django.db import models

# Create your models here.

class contact2(models.Model):
     email=models.EmailField()
     subject=models.CharField(max_length=200)
     message =models.TextField()
     def __str__(self):
      return self.email
