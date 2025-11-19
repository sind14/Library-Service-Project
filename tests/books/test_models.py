from django.test import TestCase
from .factories import BookFactory


class TestBookModel(TestCase):

    def test_str_method(self):
        book = BookFactory(title = "My Book", author = "John Doe")
        self.assertEqual(str(book), "My Book by John Doe")
