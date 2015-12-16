# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polygon',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vertex',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('polygon', models.ForeignKey(to='shapes.Polygon')),
            ],
        ),
    ]
