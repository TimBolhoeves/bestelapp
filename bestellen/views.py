from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Broodjeshuis, Walvis
from django.views.decorators.csrf import *

vandaag = date.today()
vandaag_format = vandaag.strftime("%B %d, %Y")

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def broodjeshuis(request):
    bestelling = Broodjeshuis.objects.all().values()
    template = loader.get_template('broodjeshuis.html')
    context = {
        'bestelling': bestelling,
        'datum': vandaag_format,
    }
    return HttpResponse(template.render(context, request))

def walvis(request):
    bestelling = Walvis.objects.all().values()
    template = loader.get_template('walvis.html')
    context = {
        'bestelling': bestelling,
        'datum': vandaag_format,
    }
    return HttpResponse(template.render(context, request))

def broodjeshuis_bestellen(request):
    template = loader.get_template('broodjeshuis_bestellen.html')
    return HttpResponse(template.render())

def walvis_bestellen(request):
    template = loader.get_template('walvis_bestellen.html')
    return HttpResponse(template.render())

@csrf_exempt
def broodjeshuis_bestellen_post(request):
    naam = request.POST['naam']
    nummer = request.POST['nummer']
    keuze = request.POST['keuze']
    bestelling = Broodjeshuis(naam=naam, nummer=nummer, keuze=keuze)
    bestelling.save()
    return HttpResponseRedirect(reverse('broodjeshuis'))

@csrf_exempt
def walvis_bestellen_post(request):
    naam = request.POST['naam']
    nummer = request.POST['nummer']
    keuze = request.POST['keuze']
    bestelling = Walvis(naam=naam, nummer=nummer, keuze=keuze)
    bestelling.save()
    return HttpResponseRedirect(reverse('walvis'))