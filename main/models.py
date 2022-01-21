from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    first_name = models.CharField(
        max_length=30,
        verbose_name='First name',
<<<<<<< HEAD
        default='',
        null=True
=======
        default="",
>>>>>>> tests
    )
    last_name = models.CharField(
        max_length=70,
        verbose_name='Last name',
<<<<<<< HEAD
        default='',
        null=True
=======
        default="",
>>>>>>> tests
    )
    grade = models.IntegerField(
        verbose_name='Grade',
        validators=[
            MaxValueValidator(11),
            MinValueValidator(0)
        ],
<<<<<<< HEAD
        default='',
        null=True
=======
        default="",
>>>>>>> tests
    )
    gpa = models.IntegerField(
        verbose_name='GPA',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
<<<<<<< HEAD
        default='',
        null=True
=======
        default="",
>>>>>>> tests
    )
