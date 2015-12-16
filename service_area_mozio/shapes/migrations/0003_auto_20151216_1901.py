# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0002_polygon_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polygon',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='polygon',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
