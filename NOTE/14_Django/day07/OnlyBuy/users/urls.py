from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^set_cookie/$',views.setcookie),
    url(r'^get_cookie/$',views.getcookie),
    url(r'^search/$',views.search_view),
    url(r'^mod_cookie/$',views.modcookie),
    url(r'^del_cookie/$',views.delcookie),
    url(r'^set_cookiechn/$',views.setcookiechn),
    url(r'^get_cookiechn/$',views.getcookiechn),
]