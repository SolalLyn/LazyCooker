# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 14:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_categori'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('contenu', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('jaime', models.IntegerField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('temps', models.FloatField()),
                ('cout', models.FloatField()),
                ('description', models.TextField(null=True)),
                ('besoin', models.TextField(null=True)),
                ('ingredient', models.ManyToManyField(to='website.Ingredient')),
            ],
        ),
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Section',
        ),
        migrations.RemoveField(
            model_name='article',
            name='auteur',
        ),
        migrations.RemoveField(
            model_name='article',
            name='categorie',
        ),
        migrations.DeleteModel(
            name='Categori',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='description',
            new_name='contenu',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='nom',
            new_name='titre',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='post',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Section'),
        ),
    ]
