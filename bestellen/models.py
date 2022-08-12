from django.db import models
from django.urls import reverse

class Broodjeshuis(models.Model):
    naam = models.CharField(max_length=255, default='Niet ingevuld')
    nummer = models.CharField(max_length=255, default='Niet ingevuld')
    keuze = models.TextField(default='Niet ingevuld')
    prijs = models.CharField(max_length=255, default='Niet ingevuld')
    datum = models.DateField(auto_now_add=True)
    datumExact = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.naam

    def get_absolute_url(self):
        return reverse("broodjeshuis_detail", kwargs={"pk": self.pk})
        

class Walvis(models.Model):
    naam = models.CharField(max_length=255, default='Niet ingevuld')
    nummer = models.CharField(max_length=255, default='Niet ingevuld')
    keuze = models.TextField(default='Niet ingevuld')
    prijs = models.CharField(max_length=255, default='Niet ingevuld')
    datum = models.DateField(auto_now_add=True)
    datumExact = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.naam

    def get_absolute_url(self):
        return reverse("walvis_detail", kwargs={"pk": self.pk})
