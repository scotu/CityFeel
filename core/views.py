# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from core.models import EntryClassification, Area


def ohhhhh(request):
    return HttpResponse()


def data(request):
    eq_set_all = []
    areas = []
    for a in Area.objects.all():
        areas.append({'desc': a.description, 'entries': a.entryqueue_set.filter()[:25], 'area_id': a.id})

    return render_to_response('data.html', {'areas': areas}, context_instance=RequestContext(request))

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def map(request):
    context = {'classification': EntryClassification.objects.filter(label='neg').exclude(entry__lat__isnull=True)}
    return render_to_response('map.html', context, context_instance=RequestContext(request))