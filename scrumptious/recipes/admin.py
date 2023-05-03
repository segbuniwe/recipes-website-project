from django.contrib import admin
from recipes.models import (
    Recipe,
    RecipeStep,
    RecipeIngredient,
    RecipeComment
)

# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id",
    )


@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        "recipe_title",
        "step_number",
        "instruction",
        "id",
    )


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = (
        "recipe_title",
        "amount",
        "food_item",
        "id",
    )


@admin.register(RecipeComment)
class RecipeCommentAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "recipe",
        "id",
    )
