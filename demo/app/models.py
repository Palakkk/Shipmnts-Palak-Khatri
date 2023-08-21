from django.db import models

# Create your models here.
class UserRegister(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Question(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    question = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    user=models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    comment=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)