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
    RanksSerializer,
    RanksTopoSerializer,
    RankMapSerializer,
    RankCosmoSerializer,
    ColumnsSerializer,
    ColumnsTopoSerializer,
    ColumnMapSerializer,
    ColumnCosmoSerializer,
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
    Ranks,
    RankCosmo,
    RankMap,
    RankTopo,
    Columns,
    ColumnTopo,
    ColumnMap,
    ColumnCosmo,
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
    queryset = ZoneCosmo.objects.all()
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


class NomenclaturesTopoList(generics.ListAPIView):
    queryset = NomenclatureTopo.objects.all()
    serializer_class = NomenclaturesTopoSerializer

    def get_queryset(self):
        return super().get_queryset().filter(nomenclature_id=self.kwargs["id"])


class NomenclaturesCosmoList(generics.ListAPIView):
    queryset = NomenclatureCosmo.objects.all()
    serializer_class = NomenclatureCosmoSerializer

    def get_queryset(self):
        return super().get_queryset().filter(nomenclature_id=self.kwargs["id"])


class NomenclaturesMapList(generics.ListAPIView):
    queryset = NomenclatureMap.objects.all()
    serializer_class = NomenclatureMapSerializer

    def get_queryset(self):
        return super().get_queryset().filter(nomenclature_id=self.kwargs["id"])


class RanksList(generics.ListAPIView):
    queryset = Ranks.objects.all()
    serializer_class = RanksSerializer


class RanksTopoList(generics.ListAPIView):
    queryset = RankTopo.objects.all()
    serializer_class = RanksTopoSerializer

    def get_queryset(self):
        return super().get_queryset().filter(rank_id=self.kwargs["id"])


class RanksCosmoList(generics.ListAPIView):
    queryset = RankCosmo.objects.all()
    serializer_class = RankCosmoSerializer

    def get_queryset(self):
        return super().get_queryset().filter(rank_id=self.kwargs["id"])


class RanksMapList(generics.ListAPIView):
    queryset = RankMap.objects.all()
    serializer_class = RankMapSerializer

    def get_queryset(self):
        return super().get_queryset().filter(rank_id=self.kwargs["id"])


class ColumnsList(generics.ListAPIView):
    queryset = Columns.objects.all()
    serializer_class = ColumnsSerializer


class ColumnsTopoList(generics.ListAPIView):
    queryset = ColumnTopo.objects.all()
    serializer_class = ColumnsTopoSerializer

    def get_queryset(self):
        return super().get_queryset().filter(column_id=self.kwargs["id"])


class ColumnsCosmoList(generics.ListAPIView):
    queryset = ColumnCosmo.objects.all()
    serializer_class = ColumnCosmoSerializer

    def get_queryset(self):
        return super().get_queryset().filter(column_id=self.kwargs["id"])


class ColumnsMapList(generics.ListAPIView):
    queryset = ColumnMap.objects.all()
    serializer_class = ColumnMapSerializer

    def get_queryset(self):
        return super().get_queryset().filter(column_id=self.kwargs["id"])
