import json
<<<<<<< HEAD
from django.urls import reverse

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.fields import UUIDField
from rest_framework.response import Response
from django.core import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

=======
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from django.shortcuts import render, redirect
>>>>>>> tests
from .models import Student


@api_view(['GET'])
def home(request):
<<<<<<< HEAD
    students = Student.objects.all()
    return render(
        request,
        'home.html',
        context={'students': students}
    )
=======
    students = serializers.serialize('json', Student.objects.all())
    return Response(json.loads(students))
>>>>>>> tests


@api_view(['GET', 'POST'])
def student(request):
    if request.method == 'GET':
        students = serializers.serialize('json', Student.objects.all())
        return Response(data=json.loads(students))
    if request.method == 'POST':
        new_student = Student.objects.create(**request.data)
        serializer = serializers.serialize('json', [new_student, ])
<<<<<<< HEAD
        return Response(json.loads(serializer))
=======
        return Response(data=json.loads(serializer))
>>>>>>> tests


@api_view(['GET', 'PATCH', 'DELETE'])
def student_edit(request, id):
    if request.method == 'GET':
        current_student = Student.objects.get(id=id)
        serializer = serializers.serialize('json', [current_student, ])
<<<<<<< HEAD
        return Response(json.loads(serializer))
    if request.method == 'PATCH':
        updated_student, _ = Student.objects.filter(id=id).update_or_create(**request.data)
        serializer = serializers.serialize('json', [updated_student, ])
        return Response(json.loads(serializer))
    if request.method == 'DELETE':
        Student.objects.filter(id=id).delete()
        return redirect(reverse('main:student'))
=======
        return Response(data=serializer)
    if request.method == 'PATCH':
        updated_student, _ = Student.objects.update_or_create(id=id, defaults=request.data)
        serializer = serializers.serialize('json', [updated_student, ])
        return Response(data=serializer)
    if request.method == 'DELETE':
        Student.objects.filter(id=id).delete()
        return Response()
>>>>>>> tests
