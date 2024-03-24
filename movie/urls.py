from django.urls import path
from rest_framework import routers
from movie.api.get_titles import TitleViewSet


# urlpatterns = [
#     path('title/', TitleViewSet.as_view(), name='title'),
# ]

title_router = routers.SimpleRouter()
title_router.register(
    r'title',
    TitleViewSet,
    basename='title',
)