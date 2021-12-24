from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Имя'
    )
    surname = models.CharField(
        max_length=70,
        verbose_name='Фамилия'
    )
    grade = models.IntegerField(
        verbose_name='Класс',
        validators=[
            MaxValueValidator(11),
            MinValueValidator(0)
        ])
    gpa = models.IntegerField(
        verbose_name='Средний балл',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
