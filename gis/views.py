from django.shortcuts import render

# Create your views here.
from gis.serializers import (
    ZonesSerializer,
    NomenclaturesSerializer,
    ZonesTopoSerializer,
    NomenclaturesTopoSerializer,
    ZoneCosmoSerializer,
    ZoneMapSerializer,
    NomenclaturesTopoSerializer,
    NomenclatureCosmoSerializer,
    NomenclatureMapSerializer,
)
from rest_framework import generics
from gis.models import (
    Zones,
    Nomenclatures,
    ZoneTopo,
    ZoneCosmo,
    ZoneMap,
    NomenclatureTopo,
    NomenclatureCosmo,
    NomenclatureMap,
)


class ZonesList(generics.ListAPIView):
    queryset = Zones.objects.all()
    serializer_class = ZonesSerializer


class ZonesTopoList(generics.ListAPIView):
    queryset = ZoneTopo.objects.all()
    serializer_class = ZonesTopoSerializer

    def get_queryset(self):
        return super().get_queryset().filter(zone_id=self.kwargs["id"])


class ZonesCosmoList(generics.ListAPIView):
    queryset = ZoneTopo.objects.all()
    serializer_class = ZoneCosmoSerializer

    def get_queryset(self):
        return super().get_queryset().filter(zone_id=self.kwargs["id"])


class ZonesMapList(generics.ListAPIView):
    queryset = ZoneMap.objects.all()
    serializer_class = ZoneMapSerializer

    def get_queryset(self):
        return super().get_queryset().filter(zone_id=self.kwargs["id"])


class NomenclatureList(generics.ListAPIView):
    queryset = Nomenclatures.objects.all().prefetch_related("topo", "cosmo", "map")
    serializer_class = NomenclaturesSerializer
