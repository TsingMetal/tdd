from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^([0-9]+)/$', views.view_list, name='view_list'),
    url(r'^new$', views.new_list, name='new_list'),
]
