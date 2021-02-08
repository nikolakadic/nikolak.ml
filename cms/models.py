from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=250)

class Author(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.DO_NOTHING, related_name='user')
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    birth_date = models.DateField(null=True)
    country = models.ForeignKey(Country, related_name='author_country', on_delete=models.DO_NOTHING, null=True)

class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title=models.TextField(max_length=250)
    body=models.TextField(max_length=5000)
    author= models.ForeignKey(Author, related_name='blog_author', on_delete=models.DO_NOTHING, null=True)
