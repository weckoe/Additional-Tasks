<<<<<<< HEAD
<<<<<<< HEAD
from django.urls importcd path
from .views import home, student,  student_edit
=======
=======
>>>>>>> 18cabd7fd86d622e445e07386302475624e9565e
from django.urls import path
from .views import home, student, student_edit
<<<<<<< HEAD
=======
>>>>>>> tests
>>>>>>> main

app_name = "main"

urlpatterns = [
<<<<<<< HEAD
    path("", home, name="home"),
    path("student/", student, name="student"),
    path("student_edit/<int:id>", student_edit, name="student_edit"),
<<<<<<< HEAD
=======
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
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> main
=======
>>>>>>> 18cabd7fd86d622e445e07386302475624e9565e
]
