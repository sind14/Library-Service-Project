from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .factories import BorrowingFactory
from ..books.factories import BookFactory
from ..users.factories import UserFactory


class TestBorrowingViews(APITestCase):

    def setUp(self):
        self.client: APIClient = APIClient()
        self.user = UserFactory.create()
        self.admin = UserFactory.create(is_staff=True, is_superuser=True)
        self.book = BookFactory.create(inventory=5)
        self.borrowing = BorrowingFactory.create(book=self.book, user=self.user)
        self.list_url = reverse("borrowings-list")
        self.detail_url = reverse("borrowings-detail", args=[self.borrowing.id])

    def test_user_can_list_their_borrowings(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            self.assertEqual(item["user"]["id"], self.user.id)

    def test_admin_can_list_all_borrowings(self):
        self.client.force_authenticate(self.admin)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_user_can_create_borrowing(self):
        self.client.force_authenticate(self.user)
        data = BorrowingFactory.dict(book=self.book)
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.book.refresh_from_db()
        self.assertEqual(self.book.inventory, 4)

    def test_cannot_borrow_out_of_stock_book(self):
        self.client.force_authenticate(self.user)
        self.book.inventory = 0
        self.book.save()
        data = BorrowingFactory.dict(book=self.book)
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_retrieve_own_borrowing(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.borrowing.id)

    def test_user_cannot_retrieve_others_borrowing(self):
        other_user = UserFactory.create()
        self.client.force_authenticate(other_user)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
