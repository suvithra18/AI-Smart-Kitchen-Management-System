from django.http import JsonResponse
from django.shortcuts import (render,redirect,get_object_or_404)
from django.contrib.auth.decorators import login_required
from .models import Recipe,RecipeUsage, RecipeIngredient
from .forms import RecipeForm
from .services import calculate_ingredients
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import RecipeSerializer
from .guest_ai import (
    scale_recipe
)

@login_required
def recipe_list(request):

    recipes = Recipe.objects.all()

    return render(
        request,
        'recipes/recipe_list.html',
        {'recipes': recipes}
    )


@login_required
def recipe_create(request):

    if request.method == 'POST':

        form = RecipeForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect('recipe_list')

    else:

        form = RecipeForm()

    return render(
        request,
        'recipes/recipe_create.html',
        {'form': form}
    )


@login_required
def recipe_detail(request, pk):

    recipe = get_object_or_404(
        Recipe,
        pk=pk
    )

    # VIEW COUNT

    recipe.views += 1

    recipe.save()

    # FAVORITE COUNT

    favorite_count = recipe.favorites.count()

    return render(

        request,

        'recipes/recipe_detail.html',

        {

            'recipe': recipe,

            'favorite_count': favorite_count
        }
    )

def cooking_live(request, pk):

    recipe = get_object_or_404(
        Recipe,
        pk=pk
    )

    persons = request.GET.get(

        'persons',

        recipe.base_persons
    )

    context = {

        'recipe': recipe,

        'persons': persons
    }

    return render(

        request,

        'recipes/cooking_live.html',

        context
    )

@login_required
def favorite_recipe(request, pk):

    recipe = get_object_or_404(
        Recipe,
        pk=pk
    )

    if request.user in recipe.favorites.all():

        recipe.favorites.remove(
            request.user
        )

    else:

        recipe.favorites.add(
            request.user
        )

    return redirect(

        'recipe_detail',

        pk=pk
    )


@login_required
def use_recipe(request, pk):

    recipe = Recipe.objects.get(id=pk)

    persons = int(request.GET.get("persons", 1))

    ingredients = RecipeIngredient.objects.filter(recipe=recipe)

    # Deduct stock
    for item in ingredients:

        required_qty = (item.quantity / recipe.base_persons) * persons

        item.ingredient.stock -= required_qty
        item.ingredient.save()

    # Save usage history
    RecipeUsage.objects.create(
        user=request.user,
        recipe=recipe,
        persons=persons
    )

    return redirect("recipe_list")




def recipe_cost(request, pk):

    recipe = Recipe.objects.get(
        id=pk
    )

    # =========================
    # PERSONS
    # =========================

    persons = request.GET.get(
        'persons'
    )

    if persons:

        persons = int(persons)

    else:

        persons = recipe.base_persons


    # =========================
    # SCALE FACTOR
    # =========================

    scale_factor = (

        persons /

        recipe.base_persons
    )


    # =========================
    # INGREDIENTS
    # =========================

    ingredients = RecipeIngredient.objects.filter(
        recipe=recipe
    )

    total_cost = 0

    ingredient_costs = []


    # =========================
    # CALCULATE
    # =========================

    for item in ingredients:

        scaled_quantity = (

            item.quantity *

            scale_factor
        )

        ingredient_cost = (

            scaled_quantity *

            item.ingredient.price_per_unit
        )

        total_cost += ingredient_cost

        ingredient_costs.append({

            'ingredient':
                item.ingredient.name,

            'quantity':
                round(scaled_quantity, 2),

            'unit':
                item.ingredient.unit,

            'price_per_unit':
                item.ingredient.price_per_unit,

            'ingredient_cost':
                round(ingredient_cost, 2)
        })


    # =========================
    # COST PER PERSON
    # =========================

    cost_per_person = (

        total_cost / persons

        if persons > 0

        else total_cost
    )


    # =========================
    # RENDER
    # =========================

    return render(

        request,

        'recipes/recipe_cost.html',

        {

            'recipe': recipe,

            'persons': persons,

            'ingredient_costs':
                ingredient_costs,

            'total_cost':
                round(total_cost, 2),

            'cost_per_person':
                round(cost_per_person, 2)
        }
    )

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def recipe_api(request):

    recipes = Recipe.objects.all()

    serializer = RecipeSerializer(
        recipes,
        many=True
    )

    return Response(serializer.data)
def get_recipe(request):

    recipe_name = request.GET.get(
        'recipe',
        ''
    )

    print(recipe_name)

    recipe = Recipe.objects.filter(

        name__iexact=recipe_name

    ).first()

    if recipe:

        return JsonResponse({

            'name': recipe.name,

            'description':
                recipe.description
        })

    return JsonResponse({

        'error': 'Recipe not found'
    })




def guest_scaling_dashboard(request):

    result = None

    error = None

    if request.method == 'POST':

        # =====================
        # PERSON COUNT
        # =====================

        original_persons = request.POST.get(
            'original_persons'
        )

        target_persons = request.POST.get(
            'target_persons'
        )

        # EMPTY CHECK

        if not original_persons or not target_persons:

            error = (
                'Please enter person counts'
            )

            return render(

                request,

                'recipes/guest_meal.html',

                {

                    'error': error
                }
            )

        # CONVERT

        original_persons = int(
            original_persons
        )

        target_persons = int(
            target_persons
        )

        # =====================
        # DYNAMIC INGREDIENTS
        # =====================

        ingredient_names = request.POST.getlist(
            'ingredient_name'
        )

        ingredient_quantities = request.POST.getlist(
            'ingredient_quantity'
        )

        ingredient_units = request.POST.getlist(
            'ingredient_unit'
        )

        ingredients = []

        for name, qty, unit in zip(

            ingredient_names,

            ingredient_quantities,

            ingredient_units
        ):

            if name and qty:

                ingredients.append({

                    'name': name,

                    'quantity': float(qty),

                    'unit': unit
                })

        # =====================
        # AI SCALING
        # =====================

        result = scale_recipe(

            original_persons,

            target_persons,

            ingredients
        )

    return render(

        request,

        'recipes/guest_meal.html',

        {

            'result': result,

            'error': error
        }
    )