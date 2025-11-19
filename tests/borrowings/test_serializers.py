from django.test import TestCase
from ..books.factories import BookFactory
from ..users.factories import UserFactory
from .factories import BorrowingFactory
from borrowings.serializers import BorrowingReadSerializer, BorrowingCreateSerializer


class TestBorrowingSerializer(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.book = BookFactory.create()

    def test_read_serializer(self):
        borrowing = BorrowingFactory.create(book=self.book, user=self.user)
        serializer = BorrowingReadSerializer(borrowing)
        self.assertEqual(serializer.data["id"], borrowing.id)
        self.assertEqual(serializer.data["book"]["id"], self.book.id)
        self.assertEqual(serializer.data["user"]["id"], self.user.id)

    def test_create_serializer_valid(self):
        data = BorrowingFactory.dict(book=self.book)
        context = {"request": type("Req", (), {"user": self.user})()}
        serializer = BorrowingCreateSerializer(data=data, context=context)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        borrowing = serializer.save()
        self.assertEqual(borrowing.book, self.book)
        self.assertEqual(borrowing.user, self.user)
        self.book.refresh_from_db()
        self.assertEqual(self.book.inventory, 4)

    def test_create_serializer_invalid_out_of_stock(self):
        self.book.inventory = 0
        self.book.save()
        data = BorrowingFactory.dict(book=self.book)
        context = {"request": type("Req", (), {"user": self.user})()}
        serializer = BorrowingCreateSerializer(data=data, context=context)
        self.assertFalse(serializer.is_valid())
        self.assertIn("non_field_errors", serializer.errors)
