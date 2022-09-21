from telnetlib import STATUS
from xml.parsers.expat import model
from django.db import models
# Create your models here.

class Post(models.Model):
    LANGUAGES = [
        ('chinese','CH'),
        ('english','ENG'),
        ('khmer','KM'),
        ('thai','TH')
    ]

    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100,null=True)
    album = models.CharField(max_length=100,null=True,blank=True)
    lyric = models.TextField()
    tag = models.CharField(max_length=50)
    language = models.CharField(max_length=50, choices = LANGUAGES)
    image = models.ImageField(upload_to='images/',default="default-img.jpg")
    def __str__(self):
        return self.title

class User_Report(models.Model):
    email = models.EmailField(max_length=254)
    report = models.TextField()