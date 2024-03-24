from autoslug import AutoSlugField
from uuslug import uuslug
from django.db import models


class AModel(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def instance_slug(instance):
    return instance.name

def slugify_value(value):
    return value.replace(' ', '-')


class Slugifyed(AModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(db_index=True, unique=True, populate_from=instance_slug, slugify=slugify_value)

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.slug, instance=self)
        super(Slugifyed, self).save(*args, **kwargs)
