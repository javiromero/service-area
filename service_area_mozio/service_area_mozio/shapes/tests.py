# -*- coding: utf-8 -*-
from django.test import (
    Client,
    TestCase,
)
from service_area_mozio.shapes.models import (
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

    def test_managers(self):
        """Test the default and validating managers"""
        # test using the default Manager to get invalid polygons
        qs_everything = Polygon.everything.all()
        self.assertEqual(qs_everything.count(), 2)
        # test the validating manager too
        qs_valid = Polygon.objects.all()
        self.assertEqual(qs_valid.count(), 1)

    def test_sides_property(self):
        """Test the sides property"""
        line = Polygon.everything.get(name='line')
        triangle = Polygon.everything.get(name='triangle')
        self.assertLess(line.sides, 3)
        self.assertGreaterEqual(triangle.sides, 3)

    def test_polygon_view_list(self):
        """Test the list polygon view"""
        client = Client()
        response = client.get('/shapes/')
        qs = Polygon.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['object_list']), list(qs))

    def test_polygon_view_create(self):
        """Test the create polygon view"""
        pre_count = Polygon.objects.all().count()
        client = Client()
        response = client.post(
            '/shapes/create/',
            {
                'name': 'test',
                'vertices[]': (
                    '10.10, -100.100',
                    '20.20, -200.200',
                    '30.30, -300.300',
                )
            }
        )
        post_count = Polygon.objects.all().count()
        self.assertGreater(post_count, pre_count)
