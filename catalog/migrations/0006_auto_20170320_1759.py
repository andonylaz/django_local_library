# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-20 06:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20170320_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Can mark book as returned'),)},
        ),
    ]