from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Task


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "confirm_password"]
        read_only_fields = ["id"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("El correo ya está registrado.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("El nombre de usuario ya está registrado.")
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Las contraseñas no coinciden."}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LogInSerializer(TokenObtainPairSerializer):
    pass


class TaskSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "user_id",
            "username",
            "task_title",
            "task_author",
            "task_description",
            "task_status",
            "task_due_date",
            "task_created_at",
            "task_modified_at",
        ]
        read_only_fields = [
            "id",
            "user_id",
            "username",
            "task_author",
            "task_created_at",
            "task_modified_at",
        ]

    def create(self, validated_data):
            request = self.context["request"]
            return Task.objects.create(
                user=request.user,
                task_author=request.user.username,
                **validated_data
            )