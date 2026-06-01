from django.urls import path

from .views import (
    recipe_list,
    recipe_create,
    recipe_detail,
    use_recipe,
    recipe_cost,
    recipe_api,
    get_recipe,
    guest_scaling_dashboard,
    favorite_recipe,
    cooking_live
)

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('create/', recipe_create, name='recipe_create'),
    path('<int:pk>/', recipe_detail, name='recipe_detail'),

    path('all-recipes/', recipe_api, name='all_recipes'),
    path('get-recipe/', get_recipe, name='get_recipe'),

    path('use/<int:pk>/', use_recipe, name='use_recipe'),
    path('cooking/<int:pk>/', cooking_live, name='cooking_live'),
    path('favorite/<int:pk>/', favorite_recipe, name='favorite_recipe'),
    path('recipe-cost/<int:pk>/', recipe_cost, name='recipe_cost'),

    path('api/recipes/', recipe_api, name='recipe_api'),
    path('guest-meal/', guest_scaling_dashboard, name='guest_scaling_dashboard'),
]