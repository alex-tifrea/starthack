from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_uid/$', views.get_uid, name='get_uid'),
    url(r'^(?P<uid>[a-zA-Z0-9]+)/$', views.user_info, name='user_info'),
]
