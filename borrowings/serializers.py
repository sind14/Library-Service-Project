from django.utils import timezone
from rest_framework import serializers
from .models import Borrowing
from books.serializers import BookSerializer


class BorrowingReadSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Borrowing
        fields = [
            "id",
            "user",
            "book",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
        ]


class BorrowingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ["book", "expected_return_date"]

    def validate(self, data):
        book = data["book"]
        if book.inventory <= 0:
            raise serializers.ValidationError("Book is out of stock")
        return data

    def create(self, validated_data):
        request = self.context["request"]
        book = validated_data["book"]

        book.inventory -= 1
        book.save()

        borrowing = Borrowing.objects.create(
            user=request.user,
            borrow_date=timezone.now().date(),
            **validated_data
        )
        return borrowing