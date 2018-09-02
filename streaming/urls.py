from django.conf.urls import url
from django.contrib import admin

from .views import (
	index_call,
	)


urlpatterns = [
	
	url(r'^$', index_call, name = 'streaming'),
]