from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'landing/landing_home.html')

def about(request):
    return render(request,'landing/landing_about.html')
