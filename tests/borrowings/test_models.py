from datetime import timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from ..books.factories import BookFactory
from ..users.factories import UserFactory
from .factories import BorrowingFactory


class TestBorrowingModel(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.book = BookFactory.create()
        self.today = timezone.now().date()

    def test_valid_borrowing(self):
        borrowing = BorrowingFactory.create(book=self.book, user=self.user)
        borrowing.clean()

    def test_expected_return_date_cannot_be_in_past(self):
        borrowing = BorrowingFactory.build(
            book=self.book,
            user=self.user,
            expected_return_date=self.today - timedelta(days=1)
        )
        with self.assertRaises(ValidationError):
            borrowing.clean()

    def test_actual_return_date_cannot_be_before_borrow_date(self):
        borrowing = BorrowingFactory.build(
            book=self.book,
            user=self.user,
            borrow_date=self.today,
            actual_return_date=self.today - timedelta(days=1)
        )
        with self.assertRaises(ValidationError):
            borrowing.clean()
