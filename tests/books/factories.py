import factory
from books.models import Book


class BookFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Book
        skip_postgeneration_save = True

    title = factory.Faker("sentence", nb_words=3)
    author = factory.Faker("name")
    cover = "HARD"
    inventory = 5
    daily_fee = "3.00"

    @classmethod
    def dict(cls, **kwargs):
        obj = cls.build(**kwargs)
        return {
            "title": obj.title,
            "author": obj.author,
            "cover": obj.cover,
            "inventory": obj.inventory,
            "daily_fee": str(obj.daily_fee),
        }
