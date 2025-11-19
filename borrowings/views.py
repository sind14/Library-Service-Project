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

        is_active = self.request.GET.get("is_active")
        if is_active is not None:
            if is_active.lower() == "true":
                qs = qs.filter(actual_return_date__isnull=True)
            elif is_active.lower() == "false":
                qs = qs.exclude(actual_return_date__isnull=True)

        return qs


class BorrowingDetailView(generics.RetrieveAPIView):
    serializer_class = BorrowingReadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Borrowing.objects.all()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs
