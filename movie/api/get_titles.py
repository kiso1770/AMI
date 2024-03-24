from django_restql.mixins import DynamicFieldsMixin
from rest_framework import viewsets

from movie.models import Title
from movie.serializers.title_serializer import TitleSerializer


class TitleViewSet(DynamicFieldsMixin, viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
