
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.gis.geoip2 import GeoIP2
import socket
import json



def index_call(request):
	city = get_client_ip(request)
	return render(request, 'index2.html', {'latitude':city['latitude'], 'longitude':city['longitude'], 'city':city['city']})
	#accuracy = "500ft"
	geocode = city['latitude'], city['longitude'], 
	


def get_client_ip(request):
	ip = socket.gethostbyname(socket.gethostname())
	g = GeoIP2()
	city = g.city("173.255.189.42")
	return city







	




