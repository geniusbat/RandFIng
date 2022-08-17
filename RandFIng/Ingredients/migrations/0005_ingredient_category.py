# Generated by Django 4.1 on 2022-08-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Ingredients", "0004_remove_ingredient_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredient",
            name="category",
            field=models.CharField(
                choices=[
                    ("WC", "WILDCARD"),
                    ("DA", "DAIRY"),
                    ("PR", "PROTEIN"),
                    ("ST", "STAPLE"),
                ],
                default="WC",
                max_length=2,
            ),
        ),
    ]