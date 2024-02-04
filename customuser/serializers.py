from rest_framework import serializers
from .models import CustomUserModel


class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['email', 'name', 'password']

    def create(self, validated_data):
        user = CustomUserModel.objects.create_user(**validated_data)
        return user
