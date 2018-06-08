from . import views
from django.conf.urls import url
def test(request):
	print 'in app'

urlpatterns = [
    url(r'^login$', views.index),
    url(r'^register$', views.register),
    url(r'^login_verify$', views.login_verify),
    url(r'^logout$', views.logout),

]
