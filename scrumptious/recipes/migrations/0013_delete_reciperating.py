# Generated by Django 4.2 on 2023-05-02 21:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "recipes",
            "0012_remove_reciperating_owner_remove_reciperating_rating_and_more",
        ),
    ]

    operations = [
        migrations.DeleteModel(
            name="RecipeRating",
        ),
    ]