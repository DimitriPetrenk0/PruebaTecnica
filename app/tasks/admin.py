from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "task_title",
        "task_author",
        "task_status",
        "user",
        "task_created_at",
    )
    list_filter = ("task_status", "task_created_at")
    search_fields = (
        "task_title",
        "task_description",
        "task_author",
        "user__username",
        "user__email",
    )