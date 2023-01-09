from django.db import models

# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length=300)

class Message(models.Model):
    name = models.CharField(max_length=300, verbose_name= 'Имя')
    email = models.EmailField(verbose_name= 'Почта')
    text = models.TextField(verbose_name='Сообщение')

class Project(models.Model):
    title = models.CharField(max_length=300)
    discription = models.TextField()
    image = models.ImageField(upload_to='static')
    link = models.URLField()
    
class About_me(models.Model):
    title = models.CharField(max_length=300)
