from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Цена должна быть больше или ровна 0.")
        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название не может быть пустым.")
        return value

    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
