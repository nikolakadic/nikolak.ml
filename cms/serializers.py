
from rest_framework import serializers

from .models import Author, Blog, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = []


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = []
