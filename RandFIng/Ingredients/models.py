import enum
from django.contrib.postgres.fields import ArrayField
from django.db import models

class Categories(models.TextChoices):
    WILDCARD = "WC", "WILDCARD"
    DAIRY = "DA", "DAIRY"
    PROTEIN = "PR", "PROTEIN"
    STAPLE = "ST", "STAPLE"

class Properties(models.TextChoices):
    SWEET = "Sweet"
    SPICY = "Spicy"
    VEGAN = "Vegan"
    VEGETARIAN = "Vegetarian"
    DESSERT = "Dessert"

class Ingredient(models.Model):
    name = models.CharField("Name", max_length=25)
    category = models.CharField(max_length=2 ,choices=Categories.choices)
    properties = ArrayField(models.CharField(max_length="15"), blank=True)
    class Meta:
        verbose_name = ("Ingredient")
        verbose_name_plural = ("Ingredients")
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def category(self):
        return categories[self.category]