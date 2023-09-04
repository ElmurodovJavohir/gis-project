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
    topo = ZonesTopoSerializer(many=True, read_only=True)
    cosmo = ZoneCosmoSerializer(many=True, read_only=True)
    map = ZoneMapSerializer(many=True, read_only=True)

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
    topo = NomenclaturesTopoSerializer(many=True, read_only=True)
    cosmo = NomenclatureCosmoSerializer(many=True, read_only=True)
    map = NomenclatureMapSerializer(many=True, read_only=True)

    class Meta:
        model = Nomenclatures
        fields = "__all__"
