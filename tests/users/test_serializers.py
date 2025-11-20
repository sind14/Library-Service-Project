from django.test import TestCase
from users.serializers import UserSerializer
from .factories import UserFactory

class TestUserSerializer(TestCase):

    def test_valid_create(self):
        data = UserFactory.dict()
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, data["email"])
        self.assertTrue(user.check_password(data["password"]))
