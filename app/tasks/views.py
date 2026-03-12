from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Task
from .pagination import TaskPagination
from .serializers import (
    LogInSerializer,
    UserRegistrationSerializer,
    TaskSerializer,
)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer
    permission_classes = [permissions.AllowAny]


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ["task_status"]
    search_fields = ["task_title", "task_description", "task_author"]
    ordering_fields = [
        "id",
        "task_title",
        "task_author",
        "task_status",
        "task_created_at",
        "task_modified_at",
        "task_time_remaining",
    ]
    ordering = ["-task_created_at"]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
