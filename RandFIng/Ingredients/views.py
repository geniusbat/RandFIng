from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .serializers import *
import json
from django.http import JsonResponse

def testView(request):
    data = IngredientSerializer(Ingredient.objects.all(), many=True).data
    context = {"data": json.dumps(data)}
    #context["more"] = IngredientForm()
    return render(request, "Ingredients/index.html", context)

def getAllIngredients(request):
    data = IngredientSerializer(Ingredient.objects.all(), many=True).data
    return JsonResponse(data, safe=False)