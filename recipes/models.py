from django.db import models
from django.conf import settings


class Recipe(models.Model):
    DIFFICULTY_CHOICES = [

        ('Easy', 'Easy'),

        ('Medium', 'Medium'),

        ('Hard', 'Hard')
    ]

    MEAL_TYPE_CHOICES = [

        ('Breakfast', 'Breakfast'),

        ('Lunch', 'Lunch'),

        ('Dinner', 'Dinner'),

        ('Snacks', 'Snacks'),

        ('Dessert', 'Dessert')
    ]


    FOOD_TYPE_CHOICES = [

        ('Veg', 'Veg'),

        ('Non-Veg', 'Non-Veg')
    ]


    name = models.CharField(max_length=100)
    tamil_name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    base_persons = models.IntegerField(default=2)
    servings = models.IntegerField(default=1)
    image = models.ImageField(
    upload_to='recipes/',null=True,blank=True)
    description = models.TextField()  
    cooking_time = models.IntegerField(

        default=0
    )

    difficulty = models.CharField(

        max_length=20,

        choices=DIFFICULTY_CHOICES,

        default='Easy'
    )

    cuisine_type = models.CharField(

        max_length=100,

        default='South Indian'
    )
    meal_type = models.CharField(

        max_length=20,

        choices=MEAL_TYPE_CHOICES,

        default='Lunch'
    )


    # =========================
    # VEG / NON VEG
    # =========================

    food_type = models.CharField(

        max_length=20,

        choices=FOOD_TYPE_CHOICES,

        default='Veg'
    )


    # =========================
    # POPULARITY
    # =========================

    views = models.IntegerField(
        default=0
    )

    likes = models.IntegerField(
        default=0
    )


    # =========================
    # FAVORITES
    # =========================

    favorites = models.ManyToManyField(

        settings.AUTH_USER_MODEL,

        blank=True,

        related_name='favorite_recipes'
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    stock = models.FloatField(default=0)
    UNIT_CHOICES = (
        ('g', 'Gram'),
        ('kg', 'Kilogram'),
        ('ml', 'Milliliter'),
        ('pcs', 'Pieces'),
    )
    price_per_unit = models.FloatField(default=0)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    quantity = models.FloatField()

    UNIT_CHOICES = (
        ('g', 'Gram'),
        ('kg', 'Kilogram'),
        ('ml', 'Milliliter'),
        ('pcs', 'Pieces'),
    )

    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)

    


class RecipeUsage(models.Model):

    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    persons = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

