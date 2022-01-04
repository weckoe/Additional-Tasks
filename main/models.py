from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    first_name = models.CharField(
        max_length=30,
        verbose_name='First name',
        default="",
    )
    last_name = models.CharField(
        max_length=70,
        verbose_name='Last name',
        default="",
    )
    grade = models.IntegerField(
        verbose_name='Grade',
        validators=[
            MaxValueValidator(11),
            MinValueValidator(0)
        ],
        default="",
    )
    gpa = models.IntegerField(
        verbose_name='GPA',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
        default="",
    )
