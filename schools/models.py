from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class School(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        return self.name
