import random as rd
from unicodedata import category
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

#TODO: Add gluten property
def play(request, options={"diet":"","alergies":[],"wildCards":0}):
    tags = []
    if options["diet"]=="VG":
        tags.append("VG")
    elif options["diet"]=="VE":
        tags.append("VE")
        tags.append("AP")
    if "celiac" in options["alergies"]:
        tags.append("CE")
    allIngs = Ingredient.objects.all()
    staples = allIngs.filter(category=Categories.STAPLE)
    for tag in tags:
        staples = staples.filter(properties__contains=[tag])
    staplesChosen = [staples[rd.randint(0,staples.count()-1)]]
    #Choosing dairy
    dairiesChosen = []
    if not "lactoseIntolerant" in options["alergies"]:
        dairyQ = 0
        if rd.randint(0,3)<2:
            dairyQ = 1
        dairies = allIngs.filter(category=Categories.DAIRY)
        dairiesChosen = []
        while len(dairiesChosen) < dairyQ and dairyQ!=0  and len(dairies)!=0:
            chosen = dairies[rd.randint(0,dairies.count()-1)]
            if not chosen in dairiesChosen:
                dairiesChosen.append(chosen)
    #Choosing vegetables
    vegetableQ = rd.randint(2,3)
    vegetables = allIngs.filter(category=Categories.VEGETABLE)
    for tag in tags:
        vegetables = vegetables.filter(properties__contains=[tag])
    vegetablesChosen = []
    while len(vegetablesChosen) < vegetableQ and vegetableQ!=0 and len(vegetables)!=0:
        chosen = vegetables[rd.randint(0,vegetables.count()-1)]
        if not chosen in vegetablesChosen:
            vegetablesChosen.append(chosen)
    #Choosing extras
    extrasChosen = []
    extrasQ = rd.randint(0,4) + 1-dairyQ
    extras = allIngs.filter(category=Categories.EXTRA)
    for tag in tags:
        extras = extras.filter(properties__contains=[tag])
    if extras.count()>0:
        for i in range(extrasQ):
            chosen = extras[rd.randint(0,extras.count()-1)]
            if not chosen in extrasChosen:
                extrasChosen.append(chosen)
    #Choosing protein
    proteins = allIngs.filter(category=Categories.PROTEIN)
    for tag in tags:
        proteins = proteins.filter(properties__contains=[tag])
    proteinsChosen = []
    if len(proteins)!=0:
        proteinsChosen.append(proteins[rd.randint(0,proteins.count()-1)])
    #Choosing wildcards TODO: wildcard tags
    wildcards = allIngs.filter(category=Categories.WILDCARD)
    wildcardsChosen = []
    if wildcards.count()>0:
        for ind in range(options["wildCards"]):
            wildcardsChosen = wildcards[rd.randint(0,wildcards.count()-1)]
    #Choosing condiments
    condimetsQ = rd.randint(0,3)
    condiments = allIngs.filter(properties__contains=[Properties.CONDIMENT])
    for tag in tags:
        condiments = condiments.filter(properties__contains=[tag])
    condimentsChosen = []
    while len(condimentsChosen) < condimetsQ and condimetsQ!=0 and len(condiments)!=0:
        chosen = condiments[rd.randint(0,condiments.count()-1)]
        if not chosen in condimentsChosen:
            condimentsChosen.append(chosen)
    #Fruits
    fruitsChosen = []
    fruitsQ = rd.randint(0,3)
    fruits = allIngs.filter(category=Categories.FRUIT)
    for tag in tags:
        fruits = fruits.filter(properties__contains=[tag])
    for i in range(fruitsQ):
        fruitsChosen.append(fruits[rd.randint(0,fruits.count()-1)])
    selection = {
        "staple" : staplesChosen,
        "vegetables" : vegetablesChosen,
        "protein" : proteinsChosen,
        "dairy" :  dairiesChosen,
        "extras" : extrasChosen,
        "wildCards" : wildcardsChosen,
        "condiments" : condimentsChosen,
        "fruits" : fruitsChosen
    }
    print(selection)
    context = {"data": selection}
    return render(request, "Ingredients/randomIngs.html", context)

def rulesView(request):
    context = {}
    return render(request, "rules.html", context)

def getRandomIngredient(request):
    ing = Ingredient.objects.all()[Ingredient.objects.all().count()-1]
    data = IngredientSerializer(ing).data
    return JsonResponse(data, safe=False)

def customGame(request):
    if request.method =='POST':
        options = {}
        form = request.POST
        #DietType
        if form["dietType"] == "vegetarian":
                options["diet"] = "VE"
        elif form["dietType"] == "vegan":
            options["diet"] = "VG"
        else:
            options["diet"] = ""
        if "alergies" in form:
            options["alergies"] = form["alergies"]
        else:
            options["alergies"] = []
        if "wildCardsInput" in form:
            options["wildCards"] = int(form["wildCardsAmount"])
        else:
            options["wildCards"] = 0
        return play(request, options)
    else:
        context = {}
        return render(request, "Ingredients/customGameForm.html", context)