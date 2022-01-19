from django.urls importcd path
from .views import home, student,  student_edit

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('student/', student, name='student'),
    path('student_edit/<int:id>', student_edit, name='student_edit'),
]
