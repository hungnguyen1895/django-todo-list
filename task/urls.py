from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^edit/(?P<pk>[0-9]+)$', views.TaskUpdate.as_view(), name='edit'),
	url(r'^delete/(?P<pk>[0-9]+)$', views.TaskDelete.as_view(), name='delete'),
	url(r'^complete/(?P<pk>[0-9]+)$', views.complete, name='complete'),
	
]