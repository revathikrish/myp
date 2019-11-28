from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indexpage(request):
    return HttpResponse("welcome to index")
def homepage(request):
    return HttpResponse("welcome to home page")    
def contactpage(request):
    return HttpResponse("welcome to revuuuuuus page")