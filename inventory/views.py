import json
from django.shortcuts import render, redirect,get_object_or_404
from .models import Notification, Inventory,StockHistory,ShoppingList
from django.db.models import Sum, F
from datetime import date, timedelta
from recipes.models import RecipeUsage
from .services import predict_inventory
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (InventorySerializer,ShoppingListSerializer)
from accounts.permissions import (IsAdminUserRole)
from rest_framework.permissions import (IsAuthenticated)
from rest_framework.decorators import (permission_classes)
from recipes.models import Recipe

def inventory_list(request):

    inventories = Inventory.objects.all()

    return render(
        request,
        'inventory/inventory_list.html',
        {
            'inventories': inventories
        }
    )

def add_stock(request, pk):

    inventory = get_object_or_404(
        Inventory,
        id=pk
    )

    if request.method == "POST":

        qty = float(request.POST.get("quantity"))

        inventory.quantity += qty
        inventory.save()

        # Add history
        StockHistory.objects.create(
            ingredient=inventory.ingredient,
            user=request.user,
            action='ADD',
            quantity=qty
        )

        return redirect('inventory_list')

    return render(
        request,
        'inventory/add_stock.html',
        {
            'inventory': inventory
        }
    )

def remove_stock(request, pk):

    inventory = get_object_or_404(
        Inventory,
        id=pk
    )

    if request.method == "POST":

        qty = float(request.POST.get("quantity"))

        inventory.quantity -= qty
        inventory.save()

        # Add history
        StockHistory.objects.create(
            ingredient=inventory.ingredient,
            user=request.user,
            action='REMOVE',
            quantity=qty
        )

        # LOW STOCK CHECK
        if inventory.quantity < inventory.minimum_quantity:

            ShoppingList.objects.get_or_create(

                ingredient=inventory.ingredient,

                defaults={
                    'quantity_needed':
                    inventory.minimum_quantity -
                    inventory.quantity
                }
            )

        return redirect('inventory_list')

    return render(
        request,
        'inventory/remove_stock.html',
        {
            'inventory': inventory
        }
    )

def stock_history(request):

    histories = StockHistory.objects.all().order_by('-created_at')

    return render(
        request,
        'inventory/stock_history.html',
        {
            'histories': histories
        }
    )

def shopping_list(request):

    # get low stock items
    low_stock_items = Inventory.objects.filter(
        quantity__lt=F('minimum_quantity')
    )

    # clear old shopping list
    ShoppingList.objects.all().delete()

    # create new shopping items
    for item in low_stock_items:

        needed_quantity = (
            item.minimum_quantity -
            item.quantity
        )

        ShoppingList.objects.create(

            ingredient=item.ingredient,

            quantity_needed=needed_quantity
        )

    shopping_items = ShoppingList.objects.all()

    return render(

        request,

        'inventory/shopping_list.html',

        {
            'shopping_items': shopping_items
        }
    )

def expiry_alerts(request):

    today = date.today()

    next_week = today + timedelta(days=7)

    expiring_items = Inventory.objects.filter(
        expiry_date__lte=next_week,
        expiry_date__gte=today
    )

    expired_items = Inventory.objects.filter(
        expiry_date__lt=today
    )

    return render(
        request,
        'inventory/expiry_alerts.html',
        {
            'expiring_items': expiring_items,
            'expired_items': expired_items
        }
    )

def analytics_dashboard(request):

    total_ingredients = Inventory.objects.count()

    low_stock_count = Inventory.objects.filter(
        quantity__lt=5
    ).count()

    shopping_count = ShoppingList.objects.filter(
        is_purchased=False
    ).count()

    expired_count = Inventory.objects.filter(
        expiry_date__lt=date.today()
    ).count()

    # Most used recipes
    recipe_usage = (
        RecipeUsage.objects
        .values('recipe__name')
        .annotate(total=Sum('persons'))
        .order_by('-total')[:5]
    )

    recipe_names = []
    recipe_totals = []

    for item in recipe_usage:

     recipe_names.append(item['recipe__name'])
     recipe_totals.append(item['total'])

    return render(
    request,
    'inventory/analytics_dashboard.html',
    {
        'total_ingredients': total_ingredients,
        'low_stock_count': low_stock_count,
        'shopping_count': shopping_count,
        'expired_count': expired_count,

        'recipe_names': recipe_names,
        'recipe_totals': recipe_totals,
    }
)

def ai_predictions(request):

    predictions = predict_inventory()

    return render(
        request,
        'inventory/ai_predictions.html',
        {
            'predictions': predictions
        }
    )


        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def inventory_api(request):

    inventories = Inventory.objects.all()

    serializer = InventorySerializer(
        inventories,
        many=True
    )

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([ IsAuthenticated])
def shopping_list_api(request):

    items = ShoppingList.objects.all()

    serializer = ShoppingListSerializer(
        items,
        many=True
    )

    return Response(serializer.data)

@api_view(['GET'])

@permission_classes([
    IsAdminUserRole
])

def admin_inventory_api(request):

    inventories = Inventory.objects.all()

    serializer = InventorySerializer(
        inventories,
        many=True
    )

    return Response(serializer.data)