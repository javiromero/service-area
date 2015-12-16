# -*- coding: utf-8 -*-
from django.conf.urls import url

from service_area_mozio.shapes import views

urlpatterns = [
    url(
        r'^$',
        view=views.PolygonListView.as_view(),
        name='list',
    ),
]
