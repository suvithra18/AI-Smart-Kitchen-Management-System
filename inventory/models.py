from django.db import models
from recipes.models import Ingredient
from django.conf import settings


class Notification(models.Model):

    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
    
class Inventory(models.Model):

    ingredient = models.OneToOneField(
        Ingredient,
        on_delete=models.CASCADE
    )

    quantity = models.FloatField(default=0)
    expiry_date = models.DateField(null=True,blank=True)

    minimum_quantity = models.FloatField(default=5)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.ingredient.name
    



class StockHistory(models.Model):

    ACTION_CHOICES = (
        ('ADD', 'ADD'),
        ('REMOVE', 'REMOVE'),
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    quantity = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

class ShoppingList(models.Model):

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )
    is_purchased = models.BooleanField(
        default=False
    )

    quantity_needed = models.FloatField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


