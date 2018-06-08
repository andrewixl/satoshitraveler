from . import views
from django.conf.urls import url
def test(request):
	print 'in app'

urlpatterns = [
    url(r'^login', views.index),
    url(r'^register', views.register),
    url(r'^verify', views.login),
    url(r'^logout', views.logout),

]
