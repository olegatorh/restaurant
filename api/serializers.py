from rest_framework.fields import UUIDField
from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from .models import User


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class EmployeeSerializer(ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'restaurant']


class MenuSerializer(ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())

    class Meta:
        model = Menu
        fields = ['id', 'day', 'description', 'restaurant']


class VoteMenuSerializer(ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all())
    employee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = VoteMenu
        fields = ['id', 'menu', 'restaurant', 'employee']


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token', 'restaurant']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token',)
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
