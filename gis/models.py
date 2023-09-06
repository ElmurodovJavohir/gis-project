from django.db import models
from utils.models import BaseModel


# Create your models here.
class Zones(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Zones title")

    def __str__(self):
        return self.title


class ZoneTopo(BaseModel):
    image = models.ImageField(upload_to="zones-topo", verbose_name="Zone Topo")
    zone = models.ForeignKey(
        Zones, on_delete=models.CASCADE, related_name="topo", verbose_name="Zone"
    )


class ZoneCosmo(BaseModel):
    image = models.ImageField(upload_to="zones-cosmo", verbose_name="Zone cosmo")
    zone = models.ForeignKey(
        Zones, on_delete=models.CASCADE, related_name="cosmo", verbose_name="Zone"
    )


class ZoneMap(BaseModel):
    image = models.ImageField(upload_to="zones-map", verbose_name="Zone map")
    zone = models.ForeignKey(
        Zones, on_delete=models.CASCADE, related_name="map", verbose_name="Zone"
    )


# Nomenclature


class Nomenclatures(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Nomenclatures title")

    def __str__(self):
        return self.title


class NomenclatureTopo(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Nomenclatures Topo title")
    image = models.ImageField(upload_to="nomenclatures-topo", verbose_name="Nomenclature Topo")
    nomenclature = models.ForeignKey(
        Nomenclatures, on_delete=models.CASCADE, related_name="topo", verbose_name="Nomenclature"
    )

    def __str__(self):
        return self.title


class NomenclatureCosmo(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Nomenclatures Cosmo title")
    image = models.ImageField(upload_to="nomenclatures-cosmo", verbose_name="Nomenclature cosmo")
    nomenclature = models.ForeignKey(
        Nomenclatures, on_delete=models.CASCADE, related_name="cosmo", verbose_name="Nomenclature"
    )

    def __str__(self):
        return self.title


class NomenclatureMap(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Nomenclatures Map title")
    image = models.ImageField(upload_to="nomenclatures-map", verbose_name="Nomenclature map")
    nomenclature = models.ForeignKey(
        Nomenclatures, on_delete=models.CASCADE, related_name="map", verbose_name="Nomenclature"
    )

    def __str__(self):
        return self.title


# Create your models here.
class Ranks(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Ranks title")

    def __str__(self):
        return self.title


class RankTopo(BaseModel):
    image = models.ImageField(upload_to="ranks-topo", verbose_name="Rank Topo")
    rank = models.ForeignKey(
        Ranks, on_delete=models.CASCADE, related_name="topo", verbose_name="Rank"
    )


class RankCosmo(BaseModel):
    image = models.ImageField(upload_to="ranks-cosmo", verbose_name="Rank cosmo")
    rank = models.ForeignKey(
        Ranks, on_delete=models.CASCADE, related_name="cosmo", verbose_name="Rank"
    )


class RankMap(BaseModel):
    image = models.ImageField(upload_to="ranks-map", verbose_name="Rank map")
    rank = models.ForeignKey(
        Ranks, on_delete=models.CASCADE, related_name="map", verbose_name="Rank"
    )


# Create your models here.
class Columns(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Columns title")

    def __str__(self):
        return self.title


class ColumnTopo(BaseModel):
    image = models.ImageField(upload_to="columns-topo", verbose_name="Column Topo")
    column = models.ForeignKey(
        Columns, on_delete=models.CASCADE, related_name="topo", verbose_name="Column"
    )


class ColumnCosmo(BaseModel):
    image = models.ImageField(upload_to="columns-cosmo", verbose_name="Column cosmo")
    column = models.ForeignKey(
        Columns, on_delete=models.CASCADE, related_name="cosmo", verbose_name="Column"
    )


class ColumnMap(BaseModel):
    image = models.ImageField(upload_to="columns-map", verbose_name="Column map")
    column = models.ForeignKey(
        Columns, on_delete=models.CASCADE, related_name="map", verbose_name="Column"
    )
