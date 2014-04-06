# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from core.models import EntryClassification, Area


def ohhhhh(request):
    return HttpResponse()


def data(request, id):
    a = Area.objects.get(id=int(id))
    eq_set = a.entryqueue_set.filter()[:25]
    return render_to_response('data.html', {'eq_set': eq_set}, context_instance=RequestContext(request))

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def map(request):
    context = {'classification': EntryClassification.objects.exclude(label='neutral', entry__lat__isnull=True)}
    return render_to_response('map.html', context, context_instance=RequestContext(request))