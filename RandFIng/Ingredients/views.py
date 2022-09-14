import random as rd
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .serializers import *
import json
from django.http import JsonResponse

def indexView(request):
    context = {}
    return render(request, "index.html", context)

def viewIngredients(request):
    context = {"data": Ingredient.objects.all()}
    #context["more"] = IngredientForm()
    return render(request, "Ingredients/index.html", context)

def getAllIngredients(request):
    data = IngredientSerializer(Ingredient.objects.all(), many=True).data
    return JsonResponse(data, safe=False)

#TODO: Add user chosen limits (ie: vegan only...) Add fruits!!
def play(request):
    allIngs = Ingredient.objects.all()
    staples = allIngs.filter(category=Categories.STAPLE)
    staplesChosen = staples[rd.randint(0,staples.count()-1)]
    #Choosing dairy
    dairyQ = rd.randint(0,1)
    dairies = allIngs.filter(category=Categories.DAIRY)
    dairiesChosen = []
    while len(dairiesChosen) < dairyQ and dairyQ!=0  and len(dairies)!=0:
        chosen = dairies[rd.randint(0,dairies.count()-1)]
        if not chosen in dairiesChosen:
            dairiesChosen.append(chosen)
    #Choosing vegetables
    vegetableQ = rd.randint(2,3)
    vegetables = allIngs.filter(category=Categories.VEGETABLE)
    vegetablesChosen = []
    while len(vegetablesChosen) < vegetableQ and vegetableQ!=0 and len(vegetables)!=0:
        chosen = vegetables[rd.randint(0,vegetables.count()-1)]
        if not chosen in vegetablesChosen:
            vegetablesChosen.append(chosen)
    #Choosing extras
    extras = allIngs.filter(category=Categories.EXTRA)
    extrasChosen = extras[rd.randint(0,extras.count()-1)]
    #Choosing protein
    proteins = allIngs.filter(category=Categories.PROTEIN)
    proteinsChosen = []
    if len(proteins)!=0:
        proteinsChosen = proteins[rd.randint(0,proteins.count()-1)]
    #Choosing wildcards
    wildcards = allIngs.filter(category=Categories.WILDCARD)
    wildcardsChosen = []
    if len(wildcards)!=0:
        wildcardsChosen = wildcards[rd.randint(0,wildcards.count()-1)]
    #Choosing condiments
    condimetsQ = rd.randint(0,3)
    condiments = allIngs.filter(properties__contains=[Properties.CONDIMENT])
    condimentsChosen = []
    while len(condimentsChosen) < condimetsQ and condimetsQ!=0 and len(condiments)!=0:
        chosen = condiments[rd.randint(0,condiments.count()-1)]
        if not chosen in condimentsChosen:
            condimentsChosen.append(chosen)
    selection = {
        "staple" : staplesChosen,
        "vegetables" : vegetablesChosen,
        "protein" : proteinsChosen,
        "dairy" :  dairiesChosen,
        "extras" : extrasChosen,
        "wildCards" : wildcardsChosen,
        "condiments" : condimentsChosen
    }
    print(selection)
    context = {"data": selection}
    return render(request, "Ingredients/randomIngs.html", context)

def getRandomIngredient(request):
    ing = Ingredient.objects.all()[Ingredient.objects.all().count()-1]
    data = IngredientSerializer(ing).data
    return JsonResponse(data, safe=False)
