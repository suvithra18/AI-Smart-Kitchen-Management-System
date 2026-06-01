from django.db import models


class KitchenItem(models.Model):

    UNIT_CHOICES = (

        ('kg', 'Kilogram'),

        ('g', 'Gram'),

        ('ltr', 'Liter'),

        ('ml', 'Milliliter'),

        ('pcs', 'Pieces'),
    )

    CATEGORY_CHOICES = (

        ('Vegetable', 'Vegetable'),

        ('Spice', 'Spice'),

        ('Masala', 'Masala'),

        ('Oil', 'Oil'),

        ('Grain', 'Grain'),

        ('Milk Product', 'Milk Product'),

        ('Sweet', 'Sweet'),

        ('Beverage', 'Beverage'),

        ('Other', 'Other'),
    )

    name = models.CharField(max_length=200)

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='Other'
    )

    quantity = models.FloatField(default=0)

    unit = models.CharField(
        max_length=20,
        choices=UNIT_CHOICES
    )

    

    def __str__(self):

        return self.name
    
class Recipe(models.Model):

    name = models.CharField(
        max_length=200
    )

    def __str__(self):

        return self.name


class RecipeIngredient(models.Model):

    recipe = models.ForeignKey(

        Recipe,

        on_delete=models.CASCADE
    )

    ingredient_name = models.CharField(
        max_length=200
    )

    quantity = models.FloatField()

    def __str__(self):

        return f"{self.recipe.name} - {self.ingredient_name}"