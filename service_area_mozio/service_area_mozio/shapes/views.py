# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotAllowed,
)
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from service_area_mozio.shapes.models import (
    Polygon,
    Vertex,
)
from service_area_mozio.shapes.mixins import JSONResponseMixin


class PolygonListView(JSONResponseMixin, ListView):

    """List all valid registered polygons"""
    model = Polygon
    paginate_by = 5

    def render_to_response(self, context):
        """Check format and reply accordingly"""
        if self.request.is_ajax():
            return self.render_to_json_response(context)
        else:
            return super(PolygonListView, self).render_to_response(context)


@csrf_exempt
def create_polygon(request):
    """Create a new Polygon"""
    if request.method == 'GET':
        allowed_methods = ['POST', ]
        return HttpResponseNotAllowed(allowed_methods)

    name = request.POST.get('name')
    vertices = request.POST.getlist('vertices[]')
    if len(vertices) < 3:
        msg = _(
            u'Not enought vertices.'
            u' A valid service area should have 3 or more'
        )
        response = HttpResponse(msg)
        response.status_code = 406
    else:
        shape, created = Polygon.objects.get_or_create(name=name)
        for each in vertices:
            lat, lon = each.split(',')
            shape.vertices.create(lat=lat, lon=lon)
        if not created:
            msg = _(u'Service area updated')
        else:
            msg = _(u'Service area created')
        response = HttpResponse(msg)
        response.status_code = 201

    return response
