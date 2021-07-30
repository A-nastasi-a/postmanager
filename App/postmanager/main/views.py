#from App.postmanager.main.forms import ParselForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'main/index.html', )


def about(request):
    return render(request, 'main/about.html') 

