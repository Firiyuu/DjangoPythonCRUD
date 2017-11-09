from django.conf.urls import url
from . import views

# ------------------------------------------------------------
# INDEX URL
# Description : This is the URL's for our main page.
# ------------------------------------------------------------
urlpatterns = [
    #index
    url(r'^$', views.index, name='index'),

]
