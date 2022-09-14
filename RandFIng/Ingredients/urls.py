from django.urls import path, include

from .views import *

urlpatterns = [
    path("", viewIngredients, name="ingredientsView"),
    path("play/", play),
    path("random/", getRandomIngredient, name="randomIngredientView"),
]
