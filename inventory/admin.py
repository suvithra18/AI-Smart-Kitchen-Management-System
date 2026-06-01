from django.contrib import admin
from .models import Inventory,StockHistory,ShoppingList

admin.site.register(Inventory)
admin.site.register(StockHistory)
admin.site.register(ShoppingList)