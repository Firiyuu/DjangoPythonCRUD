# -*- coding: utf-8 -*-
# !/usr/bin/python

# ------------------------------------------------------------
# Author : Phillip Andrew Espina
# Date   : 9/Nov/2017
# ------------------------------------------------------------

from crudcreate.views import Delete, Update
from django.conf.urls import url
from . import views

#Here
urlpatterns = [
    #list
    url(r'^$', views.list, name='list'),

    # Delete URL
    url(r'^list/delete/(?P<pk>\d+)/$', Delete.as_view(), name="delete"),

    # Update URL
    url(r'^list/update/(?P<pk>\d+)/$', Update.as_view(), name="update"),

    #list/<number>
    url(r'^(?P<student_id>[0-999])/$', views.detail, name='detail'),

]
