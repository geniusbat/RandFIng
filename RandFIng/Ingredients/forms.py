from django.contrib.postgres.forms import SimpleArrayField
from pyexpat import model
from django import forms
from .models import * 

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        field_classes = {
            'properties': SimpleArrayField,
        }