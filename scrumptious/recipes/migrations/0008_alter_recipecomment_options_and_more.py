# Generated by Django 4.2 on 2023-05-01 21:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0007_recipecomment_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="recipecomment",
            options={"ordering": ["created_on"]},
        ),
        migrations.AlterField(
            model_name="recipecomment",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]