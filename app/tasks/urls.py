from django.urls import path

from .views import (
    LogInView,
    UserRegistrationView,
    TaskDetailView,
    TaskListCreateView,
)

urlpatterns = [
    path("signup/", UserRegistrationView.as_view(), name="signup"),
    path("signin/", LogInView.as_view(), name="signin"),
    path("tasks/", TaskListCreateView.as_view(), name="tasks-list-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
]