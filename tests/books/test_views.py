from typing import cast
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .factories import BookFactory
from books.models import Book
from ..users.factories import UserFactory


class TestBookViews(APITestCase):

    def setUp(self):

        self.client : APIClient = APIClient()
        self.book = cast(Book, BookFactory())
        self.admin = UserFactory.create(is_superuser=True, is_staff=True)
        self.user = UserFactory.create()
        self.list_url = reverse("books-list")
        self.detail_url = reverse("books-detail", args=[self.book.id])

    def test_list_books_public(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book_public(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_create_book(self):
        self.client.force_authenticate(self.user)
        data = BookFactory.dict()
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_create_book(self):
        self.client.force_authenticate(self.admin)
        data = BookFactory.dict()
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BookFactory._meta.model.objects.count(), 2)

    def test_admin_can_update_book(self):
        self.client.force_authenticate(self.admin)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
