from django.conf import settings
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pendiente"),
        ("in_progress", "En Progreso"),
        ("completed", "Terminada"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    task_title = models.CharField(max_length=150)
    task_author = models.CharField(max_length=100, blank=True)
    task_description = models.TextField(blank=True)
    task_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    task_due_date = models.DateTimeField(null=True, blank=True)
    task_created_at = models.DateTimeField(auto_now_add=True)
    task_modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tasks"
        ordering = ["-task_created_at"]

    def __str__(self):
        return f"{self.task_title} - {self.user.username}"