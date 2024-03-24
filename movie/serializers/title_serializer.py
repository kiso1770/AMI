from django_restql.mixins import DynamicFieldsMixin
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from movie.models import Title


class TitleSerializer(DynamicFieldsMixin, ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'
