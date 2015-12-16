# -*- coding: utf-8 -*-
"""WARNING: This is obviously asking to use geodjango on it but it's not
possible for me to add it to the project with the time left to pressent it"""
from django.db import models
from django.db.models import Count
from django.utils.translation import ugettext as _


class ValidPolygonManager(models.Manager):

    """Remove invalid (<3 vertices) polygons from queryset"""
    def get_queryset(self):
        qs = super(ValidPolygonManager, self).get_queryset()
        qs_counted = qs.annotate(sides=Count('vertex')).filter(sides__gte=3)
        return qs_counted


class Polygon(models.Model):

    """A Polygon is a plane figure where three or more vertices are bound"""
    name = models.CharField(null=True, max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def sides(self):
        return self.vertex_set.count()

    def __str__(self):
        str_ = ''
        for vertex in self.vertex_set.all():
            str_ += '\n%s' % str(vertex)
        return str_

    objects = ValidPolygonManager()
    everything = models.Manager()


class Vertex(models.Model):

    """A vertex is a corner of a polygon"""
    lat = models.FloatField()
    lon = models.FloatField()
    polygon = models.ForeignKey(Polygon)

    def __str__(self):
        str_ = _("Lat: %(lat)s - Lon: %(lon)s" % {
            'lat': self.lat,
            'lon': self.lon,
        })
        return str_
