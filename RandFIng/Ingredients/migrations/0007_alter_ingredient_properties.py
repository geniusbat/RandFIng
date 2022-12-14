# Generated by Django 4.1 on 2022-08-16 11:59

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("Ingredients", "0006_alter_ingredient_category_and_more"),
    ]

    operations = [
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
                    ],
                    max_length=3,
                ),
                blank=True,
                max_length=15,
                size=None,
            ),
        ),
    ]
