# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def ohhhhh(request):
    return HttpResponse()


def data(request, id):
    return render_to_response('data.html', context_instance=RequestContext(request))

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def map(request):
    return render_to_response('map.html', context_instance=RequestContext(request))