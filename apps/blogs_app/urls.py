from django.conf.urls import url
from . import views           # This line is new!


print "i am urls.py"



urlpatterns = [
	url(r'^$', views.index),
	url(r'^(?P<id>\d+)/delete', views.delete),
	url(r'^(?P<id>\d+)/confirm', views.confirm),
	url(r'^courses/create', views.create)
	# url(r'^blogs/create$',views.create),
	# url(r'^news', views.news),
	# url(r'^(?P<number>\d+)$', views.show),
	# url(r'^(?P<number>\d+)/edit$', views.edit),
	# url(r'^(?P<number>\d+)/delete$', views.destroy)
  ]