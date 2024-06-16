from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
index_items = {
    
}



def index(request):
    return HttpResponse("Test")


def posts(request):
    return HttpResponse("Test")


def individual_post(request):
    return HttpResponse("Test")