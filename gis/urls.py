from django.urls import path, include
from gis.views import ZonesList, NomenclatureList

urlpatterns = [
    path("zones/", ZonesList.as_view()),
    path("zones/<int:id>/topo/", ZonesList.as_view()),
    path("nomenclature/", NomenclatureList.as_view()),
]
