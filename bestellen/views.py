from datetime import date, datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Broodjeshuis, Walvis
from django.views.decorators.csrf import *

DATE_FORMAT = "%Y-%m-%d"

vandaag = date.today() # + timedelta(days=1)
vandaag_format = vandaag.strftime(DATE_FORMAT)

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def broodjeshuis(request):
    bestelling = Broodjeshuis.objects.raw("SELECT * FROM bestellen_broodjeshuis WHERE datum = '{}' ".format(vandaag_format))
    template = loader.get_template('broodjeshuis.html')
    context = {
        'bestelling': bestelling,
        'datum': vandaag_format,
    }
    return HttpResponse(template.render(context, request))

def walvis(request):
    bestelling = Walvis.objects.raw("SELECT * FROM bestellen_walvis WHERE datum = '{}' ".format(vandaag_format))
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
    prijs = request.POST['prijs']
    bestelling = Broodjeshuis(naam=naam, nummer=nummer, keuze=keuze, prijs=prijs)
    bestelling.save()
    return HttpResponseRedirect(reverse('broodjeshuis'))

@csrf_exempt
def walvis_bestellen_post(request):
    naam = request.POST['naam']
    nummer = request.POST['nummer']
    keuze = request.POST['keuze']
    prijs = request.POST['prijs']
    bestelling = Walvis(naam=naam, nummer=nummer, keuze=keuze, prijs=prijs)
    bestelling.save()
    return HttpResponseRedirect(reverse('walvis'))

def betaler(request):
    bestellingbroodjes = Broodjeshuis.objects.raw("SELECT * FROM bestellen_broodjeshuis WHERE datum = '{}' ".format(vandaag_format))
    bestellingwalvis = Walvis.objects.raw("SELECT * FROM bestellen_walvis WHERE datum = '{}' ".format(vandaag_format))
    template = loader.get_template('betaler.html')
    context = {
        'bestellingwalvis': bestellingwalvis,
        'bestellingbroodjes': bestellingbroodjes,
        'datum': vandaag_format,
    }
    return HttpResponse(template.render(context, request))

def broodjeshuis_geschiedenis(request):
    bestelling = Broodjeshuis.objects.raw("SELECT * FROM bestellen_broodjeshuis ORDER BY datum DESC")
    template = loader.get_template('broodjeshuis_geschiedenis.html')
    context = {
        'bestelling': bestelling,
        'datum': vandaag_format,
    }
    return HttpResponse(template.render(context, request))

def walvis_geschiedenis(request):
    bestelling = Walvis.objects.raw("SELECT * FROM bestellen_walvis ORDER BY datum DESC")
    template = loader.get_template('walvis_geschiedenis.html')
    context = {
        'bestelling': bestelling,
        'datum': vandaag_format,
    }
    return HttpResponse(template.render(context, request))