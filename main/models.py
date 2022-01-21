from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    first_name = models.CharField(
        max_length=30,
<<<<<<< HEAD
        verbose_name="First name",
=======
        verbose_name='First name',
<<<<<<< HEAD
>>>>>>> main
        default="",
=======
<<<<<<< HEAD
        default='',
        null=True
=======
        default="",
>>>>>>> tests
>>>>>>> main
    )
    last_name = models.CharField(
        max_length=70,
<<<<<<< HEAD
        verbose_name="Last name",
=======
        verbose_name='Last name',
<<<<<<< HEAD
        default="",
=======
<<<<<<< HEAD
        default='',
        null=True
=======
>>>>>>> main
        default="",
>>>>>>> tests
>>>>>>> main
    )
    grade = models.IntegerField(
<<<<<<< HEAD
        verbose_name="Grade",
        validators=[MaxValueValidator(11), MinValueValidator(0)],
=======
        verbose_name='Grade',
        validators=[
            MaxValueValidator(11),
            MinValueValidator(0)
        ],
<<<<<<< HEAD
>>>>>>> main
        default="",
=======
<<<<<<< HEAD
        default='',
        null=True
=======
        default="",
>>>>>>> tests
>>>>>>> main
    )
    gpa = models.IntegerField(
<<<<<<< HEAD
        verbose_name="GPA",
        validators=[MaxValueValidator(10), MinValueValidator(0)],
=======
        verbose_name='GPA',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
<<<<<<< HEAD
        default="",
=======
<<<<<<< HEAD
        default='',
        null=True
=======
>>>>>>> main
        default="",
>>>>>>> tests
>>>>>>> main
    )
