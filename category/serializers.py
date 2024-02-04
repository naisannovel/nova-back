from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=1000)
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category

