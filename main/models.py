from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    first_name = models.CharField(
        max_length=30,
<<<<<<< HEAD
<<<<<<< HEAD
        verbose_name="First name",
=======
        verbose_name='First name',
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> main
=======
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
<<<<<<< HEAD
>>>>>>> main
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
<<<<<<< HEAD
>>>>>>> main
=======
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
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> main
        default="",
>>>>>>> tests
>>>>>>> main
=======
        verbose_name="First name",
        default="",
    )
    last_name = models.CharField(
        max_length=70,
        verbose_name="Last name",
        default="",
    )
    grade = models.IntegerField(
        verbose_name="Grade",
        validators=[MaxValueValidator(11), MinValueValidator(0)],
        default="",
    )
    gpa = models.IntegerField(
        verbose_name="GPA",
        validators=[MaxValueValidator(10), MinValueValidator(0)],
        default="",
>>>>>>> 18cabd7fd86d622e445e07386302475624e9565e
    )
