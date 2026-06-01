import random


# =========================
# AI CHEF RESPONSES
# =========================

RESPONSES = {

    '10 minutes': [

        'Bread Omelette',

        'Maggi',

        'Sandwich',

        'Lemon Rice',

        'Egg Fried Rice'
    ],

    'easy recipes': [

        'Tomato Rice',

        'Curd Rice',

        'Veg Fried Rice',

        'Upma'
    ],

    'breakfast': [

        'Idli',

        'Dosa',

        'Oats',

        'Pongal',

        'Bread Toast'
    ],

    'dinner': [

        'Chapathi',

        'Veg Curry',

        'Soup',

        'Fried Rice'
    ],

    'snacks': [

        'Samosa',

        'Bread Pizza',

        'French Fries',

        'Cutlet'
    ],

    'healthy': [

        'Salad',

        'Oats',

        'Sprouts',

        'Soup',

        'Green Tea'
    ],

    'kids': [

        'Chocolate Milkshake',

        'French Fries',

        'Mini Pizza',

        'Pasta'
    ],

    'veg': [

        'Paneer Curry',

        'Veg Biryani',

        'Mushroom Rice'
    ],

    'spicy': [

        'Chicken 65',

        'Spicy Fried Rice',

        'Chilli Chicken'
    ],

    'guest': [

        'Biryani',

        'Fried Rice',

        'Noodles',

        'Paneer Butter Masala'
    ]
}


# =========================
# SMART AI CHATBOT
# =========================

def chef_chatbot(message):

    text = message.lower()

    # =====================
    # QUICK COOKING
    # =====================

    if '10 minute' in text or 'quick' in text:

        recipes = RESPONSES[
            '10 minutes'
        ]

        return format_response(

            '⚡ Quick Recipes',

            recipes
        )

    # =====================
    # EASY RECIPES
    # =====================

    elif 'easy' in text or 'simple' in text:

        recipes = RESPONSES[
            'easy recipes'
        ]

        return format_response(

            '🍳 Easy Recipes',

            recipes
        )

    # =====================
    # BREAKFAST
    # =====================

    elif 'breakfast' in text:

        recipes = RESPONSES[
            'breakfast'
        ]

        return format_response(

            '🍞 Breakfast Ideas',

            recipes
        )

    # =====================
    # DINNER
    # =====================

    elif 'dinner' in text:

        recipes = RESPONSES[
            'dinner'
        ]

        return format_response(

            '🌙 Dinner Ideas',

            recipes
        )

    # =====================
    # SNACKS
    # =====================

    elif 'snack' in text:

        recipes = RESPONSES[
            'snacks'
        ]

        return format_response(

            '🍟 Snacks Ideas',

            recipes
        )

    # =====================
    # HEALTHY
    # =====================

    elif 'healthy' in text:

        recipes = RESPONSES[
            'healthy'
        ]

        return format_response(

            '🥗 Healthy Foods',

            recipes
        )

    # =====================
    # KIDS
    # =====================

    elif 'kids' in text:

        recipes = RESPONSES[
            'kids'
        ]

        return format_response(

            '🧒 Kids Favorite Foods',

            recipes
        )

    # =====================
    # VEG
    # =====================

    elif 'veg' in text or 'vegetarian' in text:

        recipes = RESPONSES[
            'veg'
        ]

        return format_response(

            '🥦 Vegetarian Recipes',

            recipes
        )

    # =====================
    # SPICY
    # =====================

    elif 'spicy' in text:

        recipes = RESPONSES[
            'spicy'
        ]

        return format_response(

            '🌶 Spicy Recipes',

            recipes
        )

    # =====================
    # GUEST
    # =====================

    elif 'guest' in text:

        recipes = RESPONSES[
            'guest'
        ]

        return format_response(

            '🍽 Guest Special Recipes',

            recipes
        )

    # =====================
    # DEFAULT
    # =====================

    return """

👨‍🍳 AI Chef Suggestions

Try Asking:

✔ What can I cook in 10 minutes?
✔ Easy recipes
✔ Healthy breakfast ideas
✔ Dinner recipes
✔ Snacks ideas
✔ Recipes for guests
✔ Vegetarian recipes
✔ Spicy foods

"""


# =========================
# RESPONSE FORMATTER
# =========================

def format_response(title, recipes):

    output = f"\n{title}\n\n"

    for recipe in recipes:

        output += f"✔ {recipe}\n"

    return output