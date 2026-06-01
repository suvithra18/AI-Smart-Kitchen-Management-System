from .models import Recipe
from .models import RecipeIngredient


# =========================
# NUTRITION DATABASE
# =========================

NUTRITION_DATA = {

    'rice': {

        'protein': 2.7,

        'carbs': 28,

        'fat': 0.3,

        'calories': 130,

        'iron': 0.2,

        'vitamins': [
            'Vitamin B'
        ]
    },

    'chicken': {

        'protein': 27,

        'carbs': 0,

        'fat': 14,

        'calories': 239,

        'iron': 1.3,

        'vitamins': [
            'Vitamin B6'
        ]
    },

    'ghee': {

        'protein': 0,

        'carbs': 0,

        'fat': 99,

        'calories': 900,

        'iron': 0,

        'vitamins': [
            'Vitamin A'
        ]
    }
}


# =========================
# RECIPE NUTRITION AI
# =========================

def calculate_recipe_nutrition(recipe_name):

    recipe = Recipe.objects.get(
        name=recipe_name
    )

    ingredients = RecipeIngredient.objects.filter(
        recipe=recipe
    )

    total_protein = 0

    total_carbs = 0

    total_fat = 0

    total_calories = 0

    total_iron = 0

    vitamins = []

    used_ingredients = []

    for item in ingredients:

        ingredient = item.ingredient_name.lower()

        quantity = item.quantity

        if ingredient in NUTRITION_DATA:

            data = NUTRITION_DATA[
                ingredient
            ]

            factor = quantity / 100

            total_protein += (
                data['protein'] * factor
            )

            total_carbs += (
                data['carbs'] * factor
            )

            total_fat += (
                data['fat'] * factor
            )

            total_calories += (
                data['calories'] * factor
            )

            total_iron += (
                data['iron'] * factor
            )

            vitamins.extend(
                data['vitamins']
            )

            used_ingredients.append(
                ingredient
            )

    return {

        'recipe': recipe.name,

        'ingredients':
            used_ingredients,

        'protein': round(
            total_protein,
            2
        ),

        'carbs': round(
            total_carbs,
            2
        ),

        'fat': round(
            total_fat,
            2
        ),

        'calories': round(
            total_calories,
            2
        ),

        'iron': round(
            total_iron,
            2
        ),

        'vitamins': list(
            set(vitamins)
        ),

        'vitamins_count': len(
            list(set(vitamins))
        )
    }