from rest_framework import generics, permissions
from .models import Borrowing
from .serializers import  BorrowingReadSerializer, BorrowingCreateSerializer


class BorrowingListView(generics.ListCreateAPIView):
    queryset = Borrowing.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BorrowingCreateSerializer
        return BorrowingReadSerializer

    def get_queryset(self):
        user = self.request.user
        qs = Borrowing.objects.all()
        if not user.is_staff:
            qs = qs.filter(user=user)
        return qs


class BorrowingDetailView(generics.RetrieveAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingReadSerializer
    permission_classes = [permissions.IsAuthenticated]
