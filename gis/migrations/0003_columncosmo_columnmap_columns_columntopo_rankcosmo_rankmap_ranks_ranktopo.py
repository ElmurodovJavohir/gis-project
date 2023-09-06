# Generated by Django 3.2 on 2023-09-06 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gis', '0002_auto_20230907_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Columns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Columns title')),
                ('title_uz', models.CharField(max_length=100, null=True, verbose_name='Columns title')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Columns title')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Columns title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ranks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Ranks title')),
                ('title_uz', models.CharField(max_length=100, null=True, verbose_name='Ranks title')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Ranks title')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Ranks title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RankTopo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='ranks-topo', verbose_name='Rank Topo')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topo', to='gis.ranks', verbose_name='Rank')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RankMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='ranks-map', verbose_name='Rank map')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map', to='gis.ranks', verbose_name='Rank')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RankCosmo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='ranks-cosmo', verbose_name='Rank cosmo')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cosmo', to='gis.ranks', verbose_name='Rank')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ColumnTopo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='columns-topo', verbose_name='Column Topo')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topo', to='gis.columns', verbose_name='Column')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ColumnMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='columns-map', verbose_name='Column map')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map', to='gis.columns', verbose_name='Column')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ColumnCosmo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='columns-cosmo', verbose_name='Column cosmo')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cosmo', to='gis.columns', verbose_name='Column')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
