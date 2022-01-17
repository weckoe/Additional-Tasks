import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from rest_framework import status
from .models import Student


@api_view(["GET"])
def home(request):
    students = serializers.serialize("json", Student.objects.all())
    return Response(json.loads(students))


@api_view(["GET", "POST"])
def student(request):
    if request.method == "GET":
        students = serializers.serialize("json", Student.objects.all())
        return Response(data=json.loads(students))
    if request.method == "POST":
        new_student = Student.objects.create(**request.data)
        serializer = serializers.serialize(
            "json",
            [
                new_student,
            ],
        )
        return Response(data=json.loads(serializer))


@api_view(["GET", "PATCH", "DELETE"])
def student_edit(request, id):
    if request.method == "GET":
        current_student = Student.objects.get(id=id)
        serializer = serializers.serialize(
            "json",
            [
                current_student,
            ],
        )
        return Response(data=serializer)
    if request.method == "PATCH":
        updated_student, _ = Student.objects.update_or_create(
            id=id, defaults=request.data
        )
        serializer = serializers.serialize(
            "json",
            [
                updated_student,
            ],
        )
        return Response(data=serializer)
    if request.method == "DELETE":
        Student.objects.filter(id=id).delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
