from django.test import TestCase
from books.serializers import BookSerializer
from .factories import BookFactory


class TestBookSerializer(TestCase):

    def test_serialization(self):
        book = BookFactory()
        serializer = BookSerializer(book)

        self.assertEqual(serializer.data["title"], book.title)
        self.assertEqual(serializer.data["author"], book.author)
        self.assertEqual(serializer.data["cover"], book.cover)
        self.assertEqual(serializer.data["inventory"], book.inventory)
        self.assertEqual(str(serializer.data["daily_fee"]), str(book.daily_fee))

    def test_validation_error_on_empty_title(self):
        data = BookFactory.dict()
        data["title"] = ""
        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)
