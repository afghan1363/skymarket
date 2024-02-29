from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """
    Переопределения Djoser-сериалайзера для регистрация пользователя
    """
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'password',)


class CurrentUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    """
    Сериалайзер для работы с зарегистрированным пользователем
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'image', 'password')
