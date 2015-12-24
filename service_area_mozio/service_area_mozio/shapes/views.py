# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse_lazy
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
from service_area_mozio.shapes.mixins import JSONjQueryResponseMixin


class PolygonListView(JSONjQueryResponseMixin, ListView):

    """List all valid registered polygons

    Used a class based view here to show it's usage with models and mixins"""
    model = Polygon
    queryset = Polygon.objects.select_related()
    paginate_by = 5

    def render_to_response(self, context):
        """Check format and reply accordingly in json or html"""
        if self.request.is_ajax():
            object_list = context['object_list']
            relations = ('vertices',)
            json_response = self.render_to_json_response(
                object_list,
                relations=relations,
            )
            return json_response
        else:
            return super(PolygonListView, self).render_to_response(context)


class PolygonDeleteView(DeleteView):

    """Delete a stored polygon"""
    model = Polygon
    success_message = _(u'Deleted Successfully')
    success_url = reverse_lazy('shapes:list')


@csrf_exempt
def create_polygon(request):
    """Create a new Polygon

    Used a function based view here to show it's usage with more complicated
    requests"""
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
        response.status_code = 400  # Bad request
    else:
        # Get polygon or create a new one
        shape, created = Polygon.objects.get_or_create(name=name)
        # Check if the vertices already belong to the shape or add them
        # FIXME: check if vertices already belong to shape before creating
        for each in vertices:
            lat, lon = each.split(',')
            shape.vertices.create(lat=lat, lon=lon)

        if not created:
            msg = _(u'Service area updated')
            status_code = 200  # Ok
        else:
            msg = _(u'Service area created')
            status_code = 201  # Created
        response = HttpResponse(msg)
        response.status_code = status_code

    return response
