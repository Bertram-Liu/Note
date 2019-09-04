from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    #  .../poll/1
    url(r'^(?P<id>\d+)/$',views.detail),
    url(r'^vote/$',views.vote,name='vote'),
    #  .../poll/1/result
    url(r'^(?P<id>\d+)/result/$', views.result)
]