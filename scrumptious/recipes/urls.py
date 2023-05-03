from django.urls import path
from recipes.views import (
    show_recipe,
    recipe_list,
    create_recipe,
    edit_recipe,
    my_recipe_list,
    create_comment,
    edit_comment,
    comment_delete,
    create_ingredient,
    create_recipe_step,
    edit_ingredient,
    edit_recipe_step,
    delete_ingredient,
    delete_step,
    delete_recipe,
)


urlpatterns = [
    path('<int:id>/', show_recipe, name="show_recipe"),
    path('', recipe_list, name="recipe_list"),
    path('create/', create_recipe, name="create_recipe"),
    path('<int:pk>/edit/', edit_recipe, name="edit_recipe"),
    path('mine/', my_recipe_list, name="my_recipe_list"),
    path('comment/', create_comment, name="create_comment"),
    path('<int:id>/edit/comment/', edit_comment, name="edit_comment"),
    path('<int:id>/delete/comment/', comment_delete, name="comment_delete"),
    path('create/ingredient/', create_ingredient, name="create_ingredient"),
    path('create/recipe-step/', create_recipe_step, name="create_recipe_step"),
    path('<int:id>/edit/ingredient/', edit_ingredient, name="edit_ingredient"),
    path('<int:id>/edit/recipe-step/', edit_recipe_step, name="edit_step"),
    path('<int:id>/delete/ingredient/', delete_ingredient, name="delete_food"),
    path('<int:id>/delete/recipe-step/', delete_step, name="delete_step"),
    path('<int:id>/delete/', delete_recipe, name="delete_recipe"),
]
