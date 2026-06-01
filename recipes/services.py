from .models import Recipe,RecipeIngredient
from inventory.utils import create_notification
from inventory.models import Inventory


def calculate_ingredients(recipe, persons):

    items = RecipeIngredient.objects.filter(recipe=recipe)

    result = []

    for item in items:

        # scale logic
        required_qty = (item.quantity / recipe.base_persons) * persons

        available = item.ingredient.stock

        result.append({
            "ingredient": item.ingredient.name,
            "required_qty": round(required_qty, 2),
            "available_stock": available,
            "unit": item.ingredient.unit,
            "status": "OK" if available >= required_qty else "LOW"
        })

    return result




def calculate_ingredients(recipe, persons):

    items = RecipeIngredient.objects.filter(recipe=recipe)

    result = []

    for item in items:

        required_qty = (item.quantity / recipe.base_persons) * persons

        available = item.ingredient.stock

        status = "OK"

        if available < required_qty:

            status = "LOW"

            create_notification(
                f"{item.ingredient.name} is LOW. Needed {required_qty}, available {available}"
            )

        result.append({
            "ingredient": item.ingredient.name,
            "required_qty": round(required_qty, 2),
            "available_stock": available,
            "unit": item.ingredient.unit,
            "status": status
        })

    return result

