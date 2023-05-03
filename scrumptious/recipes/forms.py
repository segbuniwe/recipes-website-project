from recipes.models import (Recipe,
                            RecipeComment,
                            RecipeIngredient,
                            RecipeStep,
                            )
from django.forms import ModelForm


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = (
            "title",
            "picture",
            "stars",
            "description",
        )


class RecipeCommentForm(ModelForm):
    class Meta:
        model = RecipeComment
        fields = (
            "comment",
            "recipe",
        )


class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = "__all__"


class RecipeStepForm(ModelForm):
    class Meta:
        model = RecipeStep
        fields = "__all__"
