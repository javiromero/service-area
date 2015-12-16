# -*- coding: utf-8 -*-
from django.test import TestCase
from shapes.models import (
    Polygon,
    Vertex,
)


class PolygonTestCase(TestCase):

    def setUp(self):
        """Create basic instances"""
        line = Polygon.objects.create(name='line')
        Vertex.objects.create(lat=1, lon=1, polygon=line)
        Vertex.objects.create(lat=2, lon=2, polygon=line)
        triangle = Polygon.objects.create(name='triangle')
        Vertex.objects.create(lat=1, lon=1, polygon=triangle)
        Vertex.objects.create(lat=2, lon=2, polygon=triangle)
        Vertex.objects.create(lat=3, lon=3, polygon=triangle)

    def test_min_vertices(self):
        line = Polygon.objects.get(name='line')
        triangle = Polygon.objects.get(name='triangle')
        self.assertGreater(line.sides, 3)
        self.assertGreaterEqual(triangle.sides, 3)
