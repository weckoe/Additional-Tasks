import json
from http import HTTPStatus

from django.test import TestCase, Client
from main.models import Student
from django.urls import reverse


class TestHomeView(TestCase):
    def setUp(self) -> None:
        self.student = Student.objects.create(
            id=7, first_name="Tom", last_name="Lishtvan", grade=11, gpa=10
        )

    def test_home_view(self) -> None:
        client = Client()
        url = reverse("main:home")
        response = client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.data[0]["fields"]["first_name"], "Tom")

    def test_post(self) -> None:
        client = Client()
        url = reverse("main:student")
        response = client.post(
            url,
            data={"first_name": "Kirill", "last_name": "Loxov", "grade": 6, "gpa": 5},
            content_type="application/json",
        )
        self.assertEqual(response.data[0]['fields']['first_name'], "Kirill")

    def test_student_edit_view(self) -> None:
        client = Client()
        url = reverse("main:student_edit", kwargs={"id": self.student.id})
        response = client.patch(
            url,
            data={"first_name": "Kirill", "last_name": "Loxov", "grade": 6, "gpa": 5},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.data[0]['fields']['first_name'], "Kirill")

    def test_student_delete_view(self) -> None:
        client = Client()
        url = reverse("main:student_edit", kwargs={"id": self.student.id})
        response = client.delete(
            url,
            data={"first_name": "Tom", "last_name": "Loxov", "grade": 6, "gpa": 5},
            content_type="application/json",
        )
        client.delete(url)
        self.assertEqual(response.data, HTTPStatus.NOT_FOUND)
