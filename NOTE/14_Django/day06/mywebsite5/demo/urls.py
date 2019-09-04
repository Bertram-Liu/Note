from django.conf.urls import url
from . import  views
urlpatterns = [
    url(r'^$',views.demo_views),
    url(r'^post_view/$',views.post_view,name='post_view'),
    url(r'^get_view/$',views.get_view),
    url(r'^remark/$',views.remark,name='remark')

]