from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe, RecipeComment, RecipeIngredient, RecipeStep
from recipes.forms import (RecipeForm,
                           RecipeCommentForm,
                           RecipeIngredientForm,
                           RecipeStepForm,
                           )
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            recipe.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()
    context = {
        "form": form
    }
    return render(request, "recipes/create.html", context)


def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    comments = RecipeComment.objects.filter(recipe=recipe)
    context = {
        'recipe_object': recipe,
        'comments': comments,
    }
    return render(request, 'recipes/detail.html', context)


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes,
    }
    return render(request, 'recipes/list.html', context)


@login_required
def edit_recipe(request, pk):
    recipe_object = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe_object)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=recipe_object.id)
    else:
        form = RecipeForm(instance=recipe_object)
    context = {
        "recipe_object": recipe_object,
        "form": form,
    }
    return render(request, "recipes/edit.html", context)


@login_required
def my_recipe_list(request):
    recipes = Recipe.objects.filter(author=request.user)
    context = {
        "recipe_list": recipes,
    }
    return render(request, 'recipes/list.html', context)


@login_required
def create_comment(request):
    if request.method == "POST":
        form = RecipeCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(False)
            comment.owner = request.user
            comment.save()
            return redirect("recipe_list")
    else:
        form = RecipeCommentForm()
    context = {
        "form": form,
    }
    return render(request, "recipes/create_comment.html", context)


@login_required
def edit_comment(request, id):
    recipe_comment = get_object_or_404(RecipeComment, id=id)
    recipe_detail = recipe_comment.recipe
    if request.method == "POST":
        form = RecipeCommentForm(request.POST, instance=recipe_comment)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=recipe_detail.id)
    else:
        form = RecipeCommentForm(instance=recipe_comment)
    context = {
        "recipe_comment": recipe_comment,
        "recipe_detail": recipe_detail,
        "form": form,
    }
    return render(request, "recipes/edit_comment.html", context)


@login_required
def comment_delete(request, id):
    model_instance = RecipeComment.objects.get(id=id)
    if request.method == "POST":
        model_instance.delete()
        return redirect("show_recipe", id=model_instance.recipe.id)
    context = {
        "recipe_comment": get_object_or_404(RecipeComment, id=id)
    }
    return render(request, "recipes/delete_comment.html", context)


@login_required
def create_ingredient(request):
    if request.method == "POST":
        form = RecipeIngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(False)
            ingredient.author = request.user
            ingredient.save()
            return redirect("recipe_list")
    else:
        form = RecipeIngredientForm()
    context = {
        "form": form
    }
    return render(request, "recipes/create_ingredient.html", context)


@login_required
def create_recipe_step(request):
    if request.method == "POST":
        form = RecipeStepForm(request.POST)
        if form.is_valid():
            step = form.save(False)
            step.author = request.user
            step.save()
            return redirect("recipe_list")
    else:
        form = RecipeStepForm()
    context = {
        "form": form
    }
    return render(request, "recipes/create_step.html", context)


@login_required
def edit_ingredient(request, id):
    recipe_ingredient = get_object_or_404(RecipeIngredient, id=id)
    recipe_detail = recipe_ingredient.recipe
    if request.method == "POST":
        form = RecipeIngredientForm(request.POST, instance=recipe_ingredient)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=recipe_detail.id)
    else:
        form = RecipeIngredientForm(instance=recipe_ingredient)
    context = {
        "recipe_ingredient": recipe_ingredient,
        "recipe_detail": recipe_detail,
        "form": form,
    }
    return render(request, "recipes/edit_ingredient.html", context)


@login_required
def edit_recipe_step(request, id):
    recipe_step = get_object_or_404(RecipeStep, id=id)
    recipe_detail = recipe_step.recipe
    if request.method == "POST":
        form = RecipeStepForm(request.POST, instance=recipe_step)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=recipe_detail.id)
    else:
        form = RecipeStepForm(instance=recipe_step)
    context = {
        "recipe_step": recipe_step,
        "recipe_detail": recipe_detail,
        "form": form,
    }
    return render(request, "recipes/edit_step.html", context)


@login_required
def delete_ingredient(request, id):
    model_instance = RecipeIngredient.objects.get(id=id)
    if request.method == "POST":
        model_instance.delete()
        return redirect("show_recipe", id=model_instance.recipe.id)
    context = {
        "recipe_ingredient": get_object_or_404(RecipeIngredient, id=id)
    }
    return render(request, "recipes/delete_ingredient.html", context)


@login_required
def delete_step(request, id):
    model_instance = RecipeStep.objects.get(id=id)
    if request.method == "POST":
        model_instance.delete()
        return redirect("show_recipe", id=model_instance.recipe.id)
    context = {
        "recipe_step": get_object_or_404(RecipeStep, id=id)
    }
    return render(request, "recipes/delete_step.html", context)


@login_required
def delete_recipe(request, id):
    model_instance = Recipe.objects.get(id=id)
    if request.method == "POST":
        model_instance.delete()
        return redirect("recipe_list")
    context = {
        "recipe_object": get_object_or_404(Recipe, id=id)
    }
    return render(request, "recipes/delete.html", context)
