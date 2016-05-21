from django.db import models
from django.contrib.auth.models import User
from classrooms.models import Classroom


class Student(User):
    classroom = models.ForeignKey(Classroom)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.username
