# Create your views here.
from django.shortcuts import render
def projects(request):
	return render(request, "projects.html")