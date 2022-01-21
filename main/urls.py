<<<<<<< HEAD
from django.urls importcd path
from .views import home, student,  student_edit
=======
from django.urls import path
from .views import home, student, student_edit
<<<<<<< HEAD
=======
>>>>>>> tests
>>>>>>> main

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('student/', student, name='student'),
<<<<<<< HEAD
    path('student_edit/<int:id>', student_edit, name='student_edit')
======
<<<<<<< HEAD
    path('student_edit/<int:id>', student_edit, name='student_edit'),
=======
    path('student_edit/<int:id>', student_edit, name='student_edit')
>>>>>>> tests
>>>>>>> main
]
