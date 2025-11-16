from django.urls import path
from .views import BorrowingListView, BorrowingDetailView

urlpatterns = [
    path("", BorrowingListView.as_view(), name="borrowings-list"),
    path("<int:pk>/", BorrowingDetailView.as_view(), name="borrowings-detail"),
]
