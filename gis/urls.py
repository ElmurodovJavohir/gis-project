from django.urls import path, include
from gis.views import (
    ZonesList,
    NomenclatureList,
    ZonesTopoList,
    ZonesCosmoList,
    ZonesMapList,
    NomenclaturesTopoList,
    NomenclaturesCosmoList,
    NomenclaturesMapList,
)

urlpatterns = [
    path("zones/", ZonesList.as_view()),
    path("zones/<int:id>/topo/", ZonesTopoList.as_view()),
    path("zones/<int:id>/cosmo/", ZonesCosmoList.as_view()),
    path("zones/<int:id>/map/", ZonesMapList.as_view()),
    path("nomenclature/", NomenclatureList.as_view()),
    path("nomenclature/<int:id>/topo/", NomenclaturesTopoList.as_view()),
    path("nomenclature/<int:id>/cosmo/", NomenclaturesCosmoList.as_view()),
    path("nomenclature/<int:id>/map/", NomenclaturesMapList.as_view()),
]
