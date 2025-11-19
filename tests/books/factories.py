import factory
from books.models import Book


class BookFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Book

    title = factory.Faker("sentence", nb_words=3)
    author = factory.Faker("name")
    cover = "HARD"
    inventory = 5
    daily_fee = "3.00"
