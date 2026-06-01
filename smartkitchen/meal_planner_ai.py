# =========================
# AI MEAL DATABASE
# =========================

MEAL_DATA = {

    'weight_loss': {

        'breakfast': [

            'Oats',
            'Boiled Egg',
            'Green Tea'
        ],

        'lunch': [

            'Brown Rice',
            'Grilled Chicken',
            'Salad'
        ],

        'dinner': [

            'Soup',
            'Chapathi',
            'Vegetables'
        ],

        'snacks': [

            'Fruits',
            'Nuts'
        ]
    },

    'muscle_gain': {

        'breakfast': [

            'Milk',
            'Banana',
            'Egg Omelette'
        ],

        'lunch': [

            'Chicken Rice',
            'Paneer',
            'Curd'
        ],

        'dinner': [

            'Fish',
            'Chapathi',
            'Peanut Butter'
        ],

        'snacks': [

            'Protein Shake',
            'Dry Fruits'
        ]
    },

    'weight_gain': {

        'breakfast': [
            'Peanut Butter Bread',
            'Milk'
        ],

        'lunch': [
            'Rice',
            'Chicken Curry'
        ],

        'dinner': [
            'Paneer',
            'Parotta'
        ],

        'snacks': [
            'Dry Fruits',
            'Banana Shake'
        ]
    }
}
# =========================
# AI MEAL PLANNER
# =========================

def generate_meal_plan(goal):

    return MEAL_DATA.get(
        goal,
        {}
    )