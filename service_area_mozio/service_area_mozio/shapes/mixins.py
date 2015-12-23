# -*- coding: utf-8 -*-
"""
Taken from
https://docs.djangoproject.com/en/1.8/topics/class-based-views/mixins/
"""

from django.http import HttpResponse
from service_area_mozio.shapes import serializers


class JSONResponseMixin(object):

    """A mixin that can be used to render a JSON response."""

    def render_to_json_response(self, context, **response_kwargs):
        """Returns a JSON response containing 'context' as payload"""
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
        )

    def convert_context_to_json(self, context):
        """Serialize the object, transform it into a dictionary and add the
        rendered text, then back into a json formatted string"""
        jsonSerializer = serializers.JSONSerializer()
        s_context = jsonSerializer.serialize(context, use_natural_keys=True)
        return s_context


class JSONjQueryResponseMixin(JSONResponseMixin):

    """
    Modify serializer to return null values on None
    """

    def convert_context_to_json(self, context):
        jsonSerializer = serializers.JSONjQuerySerializer()
        s_context = jsonSerializer.serialize(context, use_natural_keys=True)
        return s_context
