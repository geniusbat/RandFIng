from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from Ingredients.views import indexView, play, rulesView, customGame

from django.contrib.sitemaps.views import sitemap
from .sitemap import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("ingredients/", include("Ingredients.urls")),
    path("", indexView, name="home"),
    path("rules", rulesView, name="rules"),
    path("play", play, name="play"),
    path("customGame", customGame, name="customGame"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"Static":StaticViewSitemap,"Ingredients":IngredientSitemap}},
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
'''