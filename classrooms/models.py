from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from schools.models import School


@python_2_unicode_compatible
class Classroom(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()
    school = models.ForeignKey(School)

    class Meta:
        verbose_name = "Classroom"
        verbose_name_plural = "Classrooms"

    def __str__(self):
        return self.name
