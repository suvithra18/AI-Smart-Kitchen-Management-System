from rest_framework import serializers

from .models import (
    Inventory,
    ShoppingList
)


class InventorySerializer(serializers.ModelSerializer):

    ingredient_name = serializers.CharField(
        source='ingredient.name'
    )

    class Meta:

        model = Inventory

        fields = '__all__'


class ShoppingListSerializer(
    serializers.ModelSerializer
):

    ingredient_name = serializers.CharField(
        source='ingredient.name'
    )

    class Meta:

        model = ShoppingList

        fields = '__all__'