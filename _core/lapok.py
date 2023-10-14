from django.shortcuts import render
from Kezdolap.models import Nyilvantartas

def kezdolap(lekeres):
    nyilvantartas = Nyilvantartas.objects.all()

    return render(lekeres, 'templates/index.html',{"nyilvantartas":nyilvantartas})


