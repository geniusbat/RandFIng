from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from Ingredients.models import Ingredient

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "monthly"

    def items(self):
        return ["home", "rules", "play"]

    def location(self, item):
        return reverse(item)

class IngredientSitemap(Sitemap):
    def items(self):
        return Ingredient.objects.all()