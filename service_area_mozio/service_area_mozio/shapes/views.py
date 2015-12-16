# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from service_area_mozio.shapes.models import (
    Polygon,
    Vertex,
)


class PolygonListView(ListView):

    """List all valid registered polygons"""
    model = Polygon


class PolygonCreateView(CreateView):

    """Create a new polygon"""
    model = Polygon
