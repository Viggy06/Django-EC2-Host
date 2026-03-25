from django.urls import path
from .views import HomeAPIView, StudentListCreateAPIView, StudentDetailAPIView

urlpatterns = [
    path("", HomeAPIView.as_view()), #Testing

    path('students/', StudentListCreateAPIView.as_view()), #List and Post
    path('students/<int:pk>/', StudentDetailAPIView.as_view()), #Update and Delete
]