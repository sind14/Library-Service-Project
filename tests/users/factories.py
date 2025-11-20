import factory
from django.contrib.auth import get_user_model

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
        skip_postgeneration_save = True

    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password1234")
    is_staff = False
    is_superuser = False

    @classmethod
    def dict(cls, **kwargs):
        obj = cls.build(**kwargs)
        return {
            "email": obj.email,
            "password": "default1234",
        }
