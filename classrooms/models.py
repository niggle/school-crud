from django.db import models
from schools.models import School


class Classroom(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()
    school = models.ForeignKey(School)

    class Meta:
        verbose_name = "Classroom"
        verbose_name_plural = "Classrooms"

    def __str__(self):
        return self.name
