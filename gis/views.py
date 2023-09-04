from django.shortcuts import render

# Create your views here.
from gis.serializers import ZonesSerializer, NomenclaturesSerializer
from rest_framework import generics
from gis.models import Zones, Nomenclatures


class ZonesList(generics.ListAPIView):
    queryset = Zones.objects.all().prefetch_related("topo", "cosmo", "map")
    serializer_class = ZonesSerializer


class NomenclatureList(generics.ListAPIView):
    queryset = Nomenclatures.objects.all().prefetch_related("topo", "cosmo", "map")
    serializer_class = NomenclaturesSerializer
