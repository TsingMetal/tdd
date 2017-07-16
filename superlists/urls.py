from django.conf.urls import url, include
from django.contrib import admin

# from esop.admin import admin_site
# from lists import views
# from sign import views as sign_views


urlpatterns = [
    # url(r'^$', views.home_page, name='home'),
    # url(r'^esop/', admin_site.urls),
    # url(r'^lists/', include('lists.urls')),
    # url(r'^wechat/', include('wechat.urls')),
    # url(r'^index/$', sign_views.index),
    # url(r'^login_action/$', sign_views.login_action),
    # url(r'^event_manage/$', sign_views.event_manage),
    # url(r'^accounts/login/$', sign_views.index),
    url(r'^admin/', admin.site.urls),
]
