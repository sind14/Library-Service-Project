import factory
from django.utils import timezone
from datetime import timedelta
from ..books.factories import BookFactory
from ..users.factories import UserFactory
from borrowings.models import Borrowing


class BorrowingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Borrowing
        skip_postgeneration_save = True

    borrow_date = factory.LazyFunction(lambda: timezone.now().date())
    expected_return_date = factory.LazyFunction(lambda: timezone.now().date() + timedelta(days=7))
    actual_return_date = None
    book = factory.SubFactory(BookFactory)
    user = factory.SubFactory(UserFactory)

    @classmethod
    def dict(cls, **kwargs):
        """Словник для POST-запиту"""
        obj = cls.build(**kwargs)
        return {
            "book": obj.book.id,
            "expected_return_date": obj.expected_return_date.isoformat(),
        }
