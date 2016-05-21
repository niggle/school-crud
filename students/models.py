from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from classrooms.models import Classroom


@python_2_unicode_compatible
class Student(User):
    classroom = models.ForeignKey(Classroom)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.username
