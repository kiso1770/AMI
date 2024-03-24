from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField


# class MovieType(models.TextChoices):
#     ANIME = "ANIME", "Аниме"
#     CARTOON = "CARTOON", "Мультфильм"
#     FILM = "FILM", "Фильм"
#     SHORT = "SHORT", "Короткометражка"


class Category(models.Model):
    name = models.CharField()
    parent = models.ForeignKey('self', blank=True, related_name='children', on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Images(models.Model):
    picture = models.ImageField(upload_to='movie/series/images/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Title(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    # type = models.CharField(choices=MovieType.choices, default=MovieType.ANIME)
    picture = models.ImageField(upload_to='movie/images/', blank=True)
    description = models.TextField(blank=True)
    category = models.ManyToManyField(Category)
    release_date = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Season(models.Model):
    name = models.CharField(max_length=255)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='seasons')
    slug = AutoSlugField(unique_with=('title__name', 'name'), unique=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='movie/series/images/', blank=True)
    release_date = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.name}"


class Series(models.Model):
    name = models.CharField(max_length=255, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    title = models.ForeignKey(Title, related_name='series', on_delete=models.CASCADE)
    season = models.ForeignKey(Season, related_name='series', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    coments = models.ManyToManyField(Comment, blank=True)
    picture = models.ImageField(upload_to='movie/series/images/', blank=True)
    images = models.ManyToManyField('Images', related_name='series', blank=True)
    upload = models.FileField(upload_to='movies/series/upload/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    rating = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
