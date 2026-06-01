# =========================
# HEALTH RECIPE DATABASE
# =========================

HEALTH_RECIPES = {

    'diabetes': {

        'recommended': [

            'Brown Rice',

            'Vegetable Salad',

            'Ragi Dosa',

            'Oats',

            'Sprouts'
        ],

        'avoid': [

            'Sugar',

            'Cake',

            'Soft Drinks',

            'White Bread'
        ]
    },

    'bp': {

        'recommended': [

            'Banana',

            'Soup',

            'Salad',

            'Low Salt Chapathi'
        ],

        'avoid': [

            'Pickle',

            'High Salt Chips',

            'Fast Food'
        ]
    },

    'cholesterol': {

        'recommended': [

            'Oats',

            'Green Tea',

            'Fruits',

            'Vegetable Soup'
        ],

        'avoid': [

            'Burger',

            'Pizza',

            'Fried Chicken'
        ]
    },

    'pcod_pcos': {

    'recommended': [

        'Millets',

        'Oats',

        'Sprouts',

        'Green Leafy Vegetables',

        'Flax Seeds',

        'Fruits',

        'Brown Rice'
    ],

    'avoid': [

        'White Bread',

        'Sugar',

        'Soft Drinks',

        'Bakery Items',

        'Deep Fried Foods'
    ]
},

    'high_protein': {

        'recommended': [

            'Egg',

            'Chicken',

            'Paneer',

            'Soya',

            'Milk'
        ],

        'avoid': [

            'Junk Food',

            'Sugary Drinks'
        ]
    }
}


# =========================
# AI HEALTH RECIPE ENGINE
# =========================

def health_recipe_recommendation(
    condition
):

    return HEALTH_RECIPES.get(
        condition,
        {}
    )