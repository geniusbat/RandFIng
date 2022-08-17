from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


from .models import * 

class IngredientAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass

admin.site.register(Ingredient, IngredientAdmin)