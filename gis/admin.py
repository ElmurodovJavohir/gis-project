from django.contrib import admin
from gis.models import (
    Zones,
    ZoneCosmo,
    ZoneMap,
    ZoneTopo,
    Nomenclatures,
    NomenclatureCosmo,
    NomenclatureMap,
    NomenclatureTopo,
)

# Register your models here.
admin.site.register(
    [
        Zones,
        ZoneCosmo,
        ZoneMap,
        ZoneTopo,
        Nomenclatures,
        NomenclatureCosmo,
        NomenclatureMap,
        NomenclatureTopo,
    ]
)
