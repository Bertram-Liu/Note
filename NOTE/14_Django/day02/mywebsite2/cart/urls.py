from django.conf.urls import url
from . import views
urlpatterns = [
    #127.0.0.1:8000/cart/
    url(r'^$',views.index,),
    #127.0.0.1:8000/cart/var/
    url(r'^var/$',views.var_views),
    url(r'^filter/$',views.filter_views),
    url(r'^static/$',views.static_views),
    url(r'^base/$',views.base_views),
    url(r'^child/$',views.child_views,name='child')
]
