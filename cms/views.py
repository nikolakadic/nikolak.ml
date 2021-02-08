from rest_framework import viewsets, mixins
from rest_framework import filters

from .models import Author, Country, Blog
from .serializers import AuthorSerializer, CountrySerializer, BlogSerializer


class AuthorViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer

    search_fields = ['name', 'surname', 'languages__name']


class CountryViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    queryset = Country.objects.all().order_by('id')
    serializer_class = CountrySerializer


class BlogViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializer