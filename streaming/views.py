from django.shortcuts import render


def index_call(request):
	return render(request, "index.html", {})

