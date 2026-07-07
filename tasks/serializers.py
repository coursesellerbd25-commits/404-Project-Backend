from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "priority",
            "status",
            "selected_date",
            "due_date",
            "tags",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_tags(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Tags must be a list.")
        return value

    def validate(self, data):
        selected_date = data.get("selected_date")
        due_date = data.get("due_date")

        if (
            selected_date
            and due_date
            and due_date < selected_date
        ):
            raise serializers.ValidationError(
                {
                    "due_date": "Due date cannot be earlier than selected date."
                }
            )

        return data