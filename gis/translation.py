from modeltranslation.translator import translator, TranslationOptions
from gis.models import (
    Zones,
    Columns,
    Ranks,
    NomenclatureTopo,
    NomenclatureCosmo,
    Nomenclatures,
    NomenclatureMap,
)


class TitleTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(
    (Zones, Columns, Ranks, NomenclatureTopo, NomenclatureCosmo, Nomenclatures, NomenclatureMap),
    TitleTranslationOptions,
)
