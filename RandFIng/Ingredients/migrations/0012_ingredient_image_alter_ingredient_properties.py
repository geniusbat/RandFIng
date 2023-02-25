# Generated by Django 4.1 on 2022-10-23 15:17

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("Ingredients", "0011_alter_ingredient_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredient",
            name="image",
            field=models.ImageField(blank=True, upload_to="ingredients/"),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="properties",
            field=django_better_admin_arrayfield.models.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("SW", "Sweet"),
                        ("SP", "Spicy"),
                        ("VG", "Vegan"),
                        ("VE", "Vegetarian"),
                        ("DE", "Dessert"),
                        ("SA", "Salty"),
                        ("FI", "Fish"),
                        ("ME", "Meat"),
                        ("AP", "Animal Product"),
                        ("CO", "Condiment"),
                        ("CE", "Celiac"),
                    ],
                    max_length=3,
                ),
                blank=True,
                default=list,
                max_length=15,
                size=None,
            ),
        ),
    ]
