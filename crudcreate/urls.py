from crudcreate import views
from django.conf.urls import include, url
from crud.views import *

# ------------------------------------------------------------
# REGISTER URL's
# Description : Here's the url for the registration/create views
# ------------------------------------------------------------

urlpatterns = [
    #register
    url(r'^$', views.register, name='register'),

    # add record
    url(r'^add/', views.register, name='register'),




]