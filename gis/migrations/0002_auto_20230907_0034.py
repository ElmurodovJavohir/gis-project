# Generated by Django 3.2 on 2023-09-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomenclaturecosmo',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures Cosmo title'),
        ),
        migrations.AddField(
            model_name='nomenclaturecosmo',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures Cosmo title'),
        ),
        migrations.AddField(
            model_name='nomenclaturecosmo',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures Cosmo title'),
        ),
        migrations.AddField(
            model_name='nomenclaturemap',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures Map title'),
        ),
        migrations.AddField(
            model_name='nomenclaturemap',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures Map title'),
        ),
        migrations.AddField(
            model_name='nomenclaturemap',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures Map title'),
        ),
        migrations.AddField(
            model_name='nomenclatures',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures title'),
        ),
        migrations.AddField(
            model_name='nomenclatures',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures title'),
        ),
        migrations.AddField(
            model_name='nomenclatures',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures title'),
        ),
        migrations.AddField(
            model_name='nomenclaturetopo',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures Topo title'),
        ),
        migrations.AddField(
            model_name='nomenclaturetopo',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures Topo title'),
        ),
        migrations.AddField(
            model_name='nomenclaturetopo',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomenclatures Topo title'),
        ),
        migrations.AddField(
            model_name='zones',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Zones title'),
        ),
        migrations.AddField(
            model_name='zones',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Zones title'),
        ),
        migrations.AddField(
            model_name='zones',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Zones title'),
        ),
    ]
