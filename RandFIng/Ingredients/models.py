from django_better_admin_arrayfield.models.fields import ArrayField
from django.db import models

class Categories(models.TextChoices):
    WILDCARD = "WC", "Wild Card"
    DAIRY = "DA", "Dairy"
    PROTEIN = "PR", "Protein"
    STAPLE = "ST", "Staple"
    VEGETABLE = "VE", "Vegetable"
    EXTRA = "EX", "Extra"
    FRUIT = "FR", "Fruit"

class Properties(models.TextChoices):
    SWEET = "SW" , "Sweet"
    SPICY = "SP", "Spicy"
    VEGAN = "VG", "Vegan"
    VEGETARIAN = "VE", "Vegetarian"
    DESSERT = "DE", "Dessert"
    SALTY = "SA", "Salty"
    FISH = "FI", "Fish"
    MEAT = "ME", "Meat"
    ANIMAL_PRODUCT = "AP", "Animal Product"
    CONDIMENT = "CO", "Condiment"
    CELIAC = "CE", "Celiac"

class Ingredient(models.Model):
    name = models.CharField("Name", max_length=25)
    category = models.CharField(max_length=2 ,choices=Categories.choices, default=Categories.WILDCARD)
    properties = ArrayField(models.CharField(max_length=3, choices=Properties.choices), blank=True, max_length=15, default=list)
    
    class Meta:
        verbose_name = ("Ingredient")
        verbose_name_plural = ("Ingredients")
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def getCategory(self):
        return self.get_category_display()
    @property
    def getProperties(self):
        ret = []
        for el in self.properties:
            for choice in Properties.choices:
                if choice[0] == el:
                    ret.append(choice[1])
        return ret