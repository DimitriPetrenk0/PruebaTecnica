import django_filters

from .models import Task


class TaskFilter(django_filters.FilterSet):
    task_status = django_filters.CharFilter(
        field_name="task_status",
        lookup_expr="exact",
    )
    task_title = django_filters.CharFilter(
        field_name="task_title",
        lookup_expr="icontains",
    )
    task_author = django_filters.CharFilter(
        field_name="task_author",
        lookup_expr="icontains",
    )
    task_due_date_from = django_filters.IsoDateTimeFilter(
        field_name="task_due_date",
        lookup_expr="gte",
    )
    task_created_at_to = django_filters.IsoDateTimeFilter(
        field_name="task_created_at",
        lookup_expr="lte",
    )

    class Meta:
        model = Task
        fields = ["task_status", "task_title", "task_author"]