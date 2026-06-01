from django.contrib import admin
from .models import KitchenItem, RecipeIngredient,Recipe

admin.site.register(KitchenItem)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
