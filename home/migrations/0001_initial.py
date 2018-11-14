# Generated by Django 2.1.1 on 2018-11-14 04:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerBottom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Position')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.Image', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Banner Bottom',
                'verbose_name_plural': 'Banners Bottom',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='BannerTop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_position', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Group Position')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Banner Top',
                'verbose_name_plural': 'Banners Top',
                'ordering': ('group_position',),
            },
        ),
        migrations.CreateModel(
            name='BannerTopImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Position')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('banner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.BannerTop', verbose_name='Banner')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.Image', verbose_name='Imagem')),
            ],
        ),
    ]
