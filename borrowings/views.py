from rest_framework import generics, permissions
from .models import Borrowing
from .serializers import  BorrowingReadSerializer


class BorrowingListView(generics.ListAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingReadSerializer
    permission_classes = [permissions.IsAuthenticated]


class BorrowingDetailView(generics.RetrieveAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingReadSerializer
    permission_classes = [permissions.IsAuthenticated]
