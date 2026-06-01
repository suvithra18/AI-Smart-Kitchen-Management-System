from .models import KitchenItem


# =========================
# AI Recipe Knowledge Base
# =========================

RECIPES = {

    'Tea': {

        'ingredients': [
            'milk',
            'sugar',
            'tea powder'
        ],

        'serving_factor': 100
    },

    'Coffee': {

        'ingredients': [
            'milk',
            'sugar',
            'coffee powder'
        ],

        'serving_factor': 120
    },

    'Halwa': {

        'ingredients': [
            'wheat',
            'sugar',
            'ghee'
        ],

        'serving_factor': 150
    },

    'Payasam': {

        'ingredients': [
            'semiya',
            'milk',
            'sugar'
        ],

        'serving_factor': 200
    },

    'Pongal': {

        'ingredients': [
            'rice',
            'dal',
            'ghee'
        ],

        'serving_factor': 250
    }
}


# =========================
# DYNAMIC AI ENGINE
# =========================

def smart_recipe_generator():

    kitchen_items = KitchenItem.objects.all()

    available = {}

    for item in kitchen_items:

        available[
            item.name.lower()
        ] = item.quantity

    possible_recipes = []

    # LOOP ALL RECIPES

    for recipe_name, recipe_data in RECIPES.items():

        ingredients = recipe_data[
            'ingredients'
        ]

        matched = True

        quantities = []

        for ingredient in ingredients:

            if ingredient not in available:

                matched = False
                break

            quantities.append(
                available[ingredient]
            )

        if matched:

            minimum_qty = min(
                quantities
            )

            persons = int(

                minimum_qty /

                recipe_data[
                    'serving_factor'
                ]
            )

            if persons > 0:

                possible_recipes.append({

                    'recipe': recipe_name,

                    'persons': persons,

                    'ingredients': ingredients
                })

    return possible_recipes