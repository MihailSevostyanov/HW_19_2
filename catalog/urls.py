from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path("", product_list),
    path("contacts/", contacts),
]
