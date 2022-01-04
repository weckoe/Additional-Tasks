import json
from django.urls import reverse

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.fields import UUIDField
from rest_framework.response import Response
from django.core import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from .models import Student


def home(request):
    students = Student.objects.all()
    return render(
        request,
        'home.html',
        context={'students': students}
    )


@api_view(['GET', 'POST'])
def student(request):
    if request.method == 'GET':
        students = serializers.serialize('json', Student.objects.all())
        return Response(data=json.loads(students))
    if request.method == 'POST':
        new_student = Student.objects.create(**request.data)
        serializer = serializers.serialize('json', [new_student, ])
        return Response(json.loads(serializer))


@api_view(['GET', 'PATCH', 'DELETE'])
def student_edit(request, id):
    if request.method == 'GET':
        current_student = Student.objects.get(id=id)
        serializer = serializers.serialize('json', [current_student, ])
        return Response(json.loads(serializer))
    if request.method == 'PATCH':
        updated_student, _ = Student.objects.filter(id=id).update_or_create(**request.data)
        serializer = serializers.serialize('json', [updated_student, ])
        return Response(json.loads(serializer))
    if request.method == 'DELETE':
        Student.objects.filter(id=id).delete()
        return redirect(reverse('main:student'))
