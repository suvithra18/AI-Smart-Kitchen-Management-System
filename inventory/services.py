from recipes.models import RecipeIngredient
from .models import Inventory


def predict_inventory():

    predictions = []

    inventories = Inventory.objects.all()

    for inventory in inventories:

        ingredient = inventory.ingredient

        # estimate average daily usage
        usages = RecipeIngredient.objects.filter(
            ingredient=ingredient
        )

        total_usage = sum(
            item.quantity
            for item in usages
        )

        # fake average daily usage
        average_daily_usage = total_usage / 30 if total_usage > 0 else 1

        remaining_days = (
            inventory.quantity /
            average_daily_usage
        )

        predictions.append({

            'ingredient': ingredient.name,

            'stock': inventory.quantity,

            'average_daily_usage': round(
                average_daily_usage,
                2
            ),

            'remaining_days': round(
                remaining_days,
                1
            ),

            'status':
                'CRITICAL'
                if remaining_days < 3
                else 'STABLE'
        })

    return predictions