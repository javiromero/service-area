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
        # test using the default Manager to get invalid polygons
        line = Polygon.everything.get(name='line')
        triangle = Polygon.everything.get(name='triangle')
        self.assertLess(line.sides, 3)
        self.assertGreaterEqual(triangle.sides, 3)
        # test the validating manager too
        qs = Polygon.objects.all()
        self.assertEqual(qs.count(), 1)
