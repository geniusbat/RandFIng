# Generated by Django 4.1 on 2022-10-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Ingredients", "0012_ingredient_image_alter_ingredient_properties"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="image",
            field=models.CharField(
                blank=True, default=None, max_length=25, verbose_name="image"
            ),
        ),
    ]