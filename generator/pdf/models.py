from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)  # Use EmailField for emails
    phone = models.CharField(max_length=200,null=True)
    summary =models.TextField(default='')
    degree = models.CharField(max_length=200,null=True)
    school = models.CharField(max_length=200,null=True)
    university = models.CharField(max_length=200,null=True)
    previous_work = models.TextField(default='')  # No max_length for TextField
    skills = models.TextField(default='')  # No max_length for TextField
