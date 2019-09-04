from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index),
    url('^(?P<id>\d+)/$', views.detail),
    url('^(?P<id>\d+)/result/$', views.result)
]