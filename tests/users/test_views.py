from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from .factories import UserFactory


class TestUserViews(APITestCase):

    def setUp(self):
        self.client: APIClient = APIClient()
        self.admin = get_user_model().objects.create_superuser(email="admin@test.com", password="admin1234")
        self.user = get_user_model().objects.create_user(email="user@test.com", password="user1234")
        self.list_url = reverse("users-list")
        self.create_url = reverse("users-list")

    def test_user_can_register(self):
        data = UserFactory.dict()
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_admin_can_list_users(self):
        self.client.force_authenticate(self.admin)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_regular_user_cannot_list_users(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
