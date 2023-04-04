from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=100, primary_key=True)

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)