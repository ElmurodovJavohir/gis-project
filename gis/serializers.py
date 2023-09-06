from rest_framework import serializers
from gis.models import (
    Zones,
    ZoneCosmo,
    ZoneMap,
    ZoneTopo,
    Nomenclatures,
    NomenclatureCosmo,
    NomenclatureMap,
    NomenclatureTopo,
    Ranks,
    RankCosmo,
    RankMap,
    RankTopo,
    Columns,
    ColumnCosmo,
    ColumnMap,
    ColumnTopo,
)


class ZoneMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneMap
        fields = "__all__"


class ZoneCosmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneCosmo
        fields = "__all__"


class ZonesTopoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneTopo
        fields = "__all__"


class ZonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zones
        fields = "__all__"


class NomenclatureMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = NomenclatureMap
        fields = "__all__"


class NomenclatureCosmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NomenclatureCosmo
        fields = "__all__"


class NomenclaturesTopoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NomenclatureTopo
        fields = "__all__"


class NomenclaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomenclatures
        fields = "__all__"


class RankMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankMap
        fields = "__all__"


class RankCosmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankCosmo
        fields = "__all__"


class RanksTopoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankTopo
        fields = "__all__"


class RanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranks
        fields = "__all__"


class ColumnMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnMap
        fields = "__all__"


class ColumnCosmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnCosmo
        fields = "__all__"


class ColumnsTopoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnTopo
        fields = "__all__"


class ColumnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Columns
        fields = "__all__"
