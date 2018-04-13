# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-13 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20180413_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='item',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.AddField(
            model_name='item',
            name='wishlist',
            field=models.ManyToManyField(related_name='wish_items', to='myApp.Wishlist'),
        ),
        migrations.AddField(
            model_name='user',
            name='wishlist',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myApp.Wishlist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_items', to='myApp.User'),
        ),
    ]