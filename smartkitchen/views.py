from django.shortcuts import render


from .ai_engine import (
    smart_recipe_generator
)
from .nutrition_ai import (
    calculate_recipe_nutrition
)
from .health_ai import (
    health_recommendation
)
from .meal_planner_ai import (
    generate_meal_plan
)
from .leftover_recipe_ai import (
    leftover_transformation
)
from .health_recipe_ai import (
    health_recipe_recommendation
)
from .chatbot_ai import (
    chef_chatbot
)
from .carbon_ai import (
    calculate_carbon_footprint
)
def smart_kitchen(request):

    return render(

        request,

        'smartkitchen/dashboard.html'
    )

def smart_ai(request):

    recipes = smart_recipe_generator()

    return render(

        request,

        'smartkitchen/smart_ai.html',

        {
            'recipes': recipes
        }
    )

def voice_assistant(request):

    return render(

        request,

        'smartkitchen/voice_assistant.html'
    )

def nutrition_dashboard(request):

    nutrition = None

    recommendations = []

    recipe_name = request.GET.get(
        'recipe'
    )

    if recipe_name:

        nutrition = calculate_recipe_nutrition(
            recipe_name
        )

        recommendations = health_recommendation(
            nutrition
        )

    return render(

        request,

        'smartkitchen/nutrition.html',

        {

            'nutrition': nutrition,

            'recommendations':
                recommendations
        }
    )

def ai_meal_planner(request):

    meal_plan = None

    goal = request.GET.get(
        'goal'
    )

    if goal:

        meal_plan = generate_meal_plan(
            goal
        )

    return render(

        request,

        'smartkitchen/meal_planner.html',

        {

            'meal_plan': meal_plan,

            'goal': goal
        }
    )
def leftover_transform_dashboard(request):

    suggestions = (
        leftover_transformation()
    )

    return render(

        request,

        'smartkitchen/leftover_transform.html',

        {

            'suggestions':
                suggestions
        }
    )


def health_recipe_dashboard(request):

    result = None

    condition = request.GET.get(
        'condition'
    )

    if condition:

        result = (
            health_recipe_recommendation(
                condition
            )
        )

    return render(

        request,

        'smartkitchen/health_recipe.html',

        {

            'result': result,

            'condition': condition
        }
    )

def ai_chef_chatbot(request):

    response = None

    if request.method == 'POST':

        message = request.POST.get(
            'message'
        )

        response = chef_chatbot(
            message
        )

    return render(

        request,

        'smartkitchen/chef_chatbot.html',

        {

            'response': response
        }
    )

def carbon_dashboard(request):

    result = (
        calculate_carbon_footprint()
    )

    return render(

        request,

        'smartkitchen/carbon_dashboard.html',

        {

            'result': result
        }
    )