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


class PolygonListView(ListView):

    """List all valid registered polygons"""
    model = Polygon


@csrf_exempt
def create_polygon(request):
    """Create a new Polygon"""
    if request.method == 'GET':
        allowed_methods = ['POST', ]
        return HttpResponseNotAllowed(allowed_methods)

    response_dict = {
        'success': False,
        'msg': '',
    }
    name = request.POST.get('name')
    vertices = request.POST.getlist('vertices[]')
    if len(vertices) < 3:
        success = False
        msg = _(
            u'Not enought vertices.'
            u' A valid service area should have 3 or more'
        )
    else:
        shape = Polygon.objects.create(name=name)
        for each in vertices:
            lat, lon = each.split(',')
            shape.vertices.create(lat=lat, lon=lon)
        success = True
        msg = _(u'Service area created')

    response_dict['success'] = success
    response_dict['msg'] = msg
    return HttpResponse(
        json.dumps(response_dict),
        content_type='application/json'
    )
