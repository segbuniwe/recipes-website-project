from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    stars = models.CharField(max_length=20, default="4.3 stars")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='recipes',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title


class RecipeStep(models.Model):
    step_number = models.PositiveSmallIntegerField()
    instruction = models.TextField()
    recipe = models.ForeignKey(
        'Recipe',
        related_name='steps',
        on_delete=models.CASCADE,
    )

    def recipe_title(self):
        return self.recipe.title

    class Meta:
        ordering = ['step_number']


class RecipeIngredient(models.Model):
    amount = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        'Recipe',
        related_name='ingredients',
        on_delete=models.CASCADE,
    )

    def recipe_title(self):
        return self.recipe.title

    class Meta:
        ordering = ['food_item']


class RecipeComment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(
        'Recipe',
        related_name='comments',
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE,
        null=True,
    )

    def recipe_title(self):
        return self.recipe.title

    class Meta:
        ordering = ['-created_on']
