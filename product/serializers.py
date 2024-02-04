from rest_framework import serializers
from .models import Product
from category.models import Category


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=1000)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product
