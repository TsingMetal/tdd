from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^([0-9]+)/$', views.view_list, name='view_list'),
    url(r'^([0-9]+)/add_item$', views.add_item, name='add_item'),
    url(r'^new$', views.new_list, name='new_list'),
]
