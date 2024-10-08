from django.core.management.base import BaseCommand, CommandError

import csv
from Ingredients.models import Categories, Properties, Ingredient
from django.conf import settings
from pathlib import Path

class Command(BaseCommand):
    help = 'Command to add ingredients from csv'

    def add_arguments(self, parser):
        parser.add_argument('fileDir', nargs='+', type=str)

    def handle(self, *args, **options):
        fileDir = options['fileDir']
        try:
            read(fileDir[0])
        except Exception as e:
            raise CommandError("Something went wrong: " + str(e))
        self.stdout.write(self.style.SUCCESS("Finished succesfully!"))

def read(fileDir=""):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    categories = {
        "fruit": "FR",
        "dairy": "DA",
        "extra" : "EX",
        "staple" : "ST",
        "protein" : "PR",
        "wild card" : "WC",
        "vegetable" : "VE",
        "fruit" : "FR"
    }
    properties = {
        "sweet" : "SW",
        "animal product" : "AP",
        "vegetarian" : "VE",
        "vegan" : "VG",
        "spicy" : "SP",
        "condiment" : "CO",
        "dessert" : "DE",
        "salty" : "SA",
        "meat" : "ME",
        "fish" : "FI",
        "celiac" : "CE"
    }
    if fileDir=="":
        fileDir="ingredients.csv"
    print(fileDir)
    with open(fileDir) as file:
        reader = csv.reader(file, delimiter=',')
        firstLine = True
        for row in reader:
            #Ignore first line 
            if firstLine:
                firstLine=False
            else:
                csvName = row[0].strip().lower().capitalize()
                rawCategory = row[1].strip().lower()
                if rawCategory in categories:
                    csvCategory=categories[rawCategory]
                else:
                    print("ALERT!: "+str(rawCategory)+" not found")
                rawCsvProperties = row[2].strip().lower().split(";")
                csvProperties = []
                for rawProperty in rawCsvProperties:
                    prop = rawProperty.strip()
                    if prop in properties:
                        csvProperties.append(properties[prop])
                    else:
                        print("ALERT!: "+str(prop)+" not found")
                print("{}, {}, {}".format(csvName, csvCategory, csvProperties))
                ing = Ingredient(name=csvName, category=csvCategory, properties=csvProperties)
                if row[3].strip() != "":
                    p = "\\ingredients\\" + row[3].strip() + ".jpg"
                else:
                    p =  "\\ingredients\\" + csvName.lower() + ".jpg"
                ing.image = p
                ing.save()

#read(r"C:\Users\PC\Documents\Proyectos\Programacion\RandFIng\RandFIng\Ingredients.csv")