from django.urls import path

from .views import smart_kitchen ,smart_ai,voice_assistant,nutrition_dashboard,ai_meal_planner,leftover_transform_dashboard,health_recipe_dashboard,ai_chef_chatbot,carbon_dashboard


urlpatterns = [
     path(

        '',

        smart_kitchen,

        name='smart_kitchen'
    ),
     path(
        'smart-ai/',
        smart_ai,
        name='smart_ai'
    ),
    path(
    'voice-assistant/',
    voice_assistant,
    name='voice_assistant'
),
 path(
        'nutrition/',
        nutrition_dashboard,
        name='nutrition_dashboard'
    ),
    path(
    'meal-planner/',
    ai_meal_planner,
    name='ai_meal_planner'
),

path(

    'leftover-transform/',

    leftover_transform_dashboard,

    name='leftover_transform_dashboard'
),
path(

    'health-recipes/',

    health_recipe_dashboard,

    name='health_recipe_dashboard'
),
path(

    'ai-chef/',

    ai_chef_chatbot,

    name='ai_chef_chatbot'
),
path(

    'carbon-dashboard/',

    carbon_dashboard,

    name='carbon_dashboard'
),

]