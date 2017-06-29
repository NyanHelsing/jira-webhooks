# -*- coding: utf-8 -*-
"""REST API URLs"""


from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from api import views


urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
])
