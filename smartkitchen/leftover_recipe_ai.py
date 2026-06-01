from .models import KitchenItem


# =========================
# LEFTOVER TRANSFORMATION AI
# =========================

LEFTOVER_RECIPES = {

    'rice': [

        'Lemon Rice',

        'Tomato Rice',

        'Vegetable Fried Rice',

        'Curd Rice'
    ],

    'chapathi': [

        'Kothu Chapathi',

        'Chapathi Noodles'
    ],

    'idli': [

        'Fried Idli',

        'Idli Upma'
    ],

    'vegetables': [

        'Vegetable Rice',

        'Mixed Veg Curry',

        'Veg Soup'
    ],

    'chicken': [

        'Chicken Fried Rice',

        'Chicken Soup',

        'Chicken Sandwich'
    ],

    'bread': [

        'Bread Upma',

        'Bread Pizza',

        'Bread Toast'
    ]
}


# =========================
# SMART LEFTOVER ENGINE
# =========================

def leftover_transformation():

    kitchen_items = KitchenItem.objects.all()

    suggestions = []

    for item in kitchen_items:

        ingredient = item.name.lower()

        quantity = item.quantity

        # ONLY LEFTOVER ITEMS

        if quantity > 0:

            # EXACT MATCH

            if ingredient in LEFTOVER_RECIPES:

                recipes = LEFTOVER_RECIPES[
                    ingredient
                ]

                suggestions.append({

                    'ingredient': ingredient,

                    'recipes': recipes
                })

            # VEGETABLE DETECTION

            elif ingredient in [

                'carrot',

                'beans',

                'cabbage',

                'onion',

                'capsicum',

                'peas'

            ]:

                suggestions.append({

                    'ingredient': ingredient,

                    'recipes': [

                        'Vegetable Rice',

                        'Veg Noodles',

                        'Veg Soup'
                    ]
                })

    return suggestions