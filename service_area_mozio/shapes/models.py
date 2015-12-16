# -*- coding: utf-8 -*-
"""WARNING: This is obviously asking to use geodjango on it but it's not
possible for me to add it to the project with the time left to pressent it"""
from django.db import models


class Polygon(models.Model):

    """A Polygon is a plane figure where three or more vertices are bound"""
    name = models.CharField(null=True, max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Vertex(models.Model):

    """A vertex is a corner of a polygon"""
    lat = models.FloatField()
    lon = models.FloatField()
    polygon = models.ForeignKey(Polygon)
