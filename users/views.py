from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        if self.action in ["list", "destroy"]:
            return [IsAdminUser()]

        return super().get_permissions()
