from django.shortcuts import render, redirect
from Kezdolap.models import Nyilvantartas

def kezdolap(request):
    nyilvantartas = Nyilvantartas.objects.all()
    return render(request, 'index.html', {"nyilvantartas": nyilvantartas})

def uj_adat(request):
    if request.method == "POST":
        vezetek_nev = request.POST.get('vezetek_nev')
        kereszt_nev = request.POST.get('kereszt_nev')
        kulcs_szam = request.POST.get('kulcs_szam')

        nyilvantartas = Nyilvantartas(vezetek_nev=vezetek_nev, kereszt_nev=kereszt_nev, kulcs_szam=kulcs_szam)
        nyilvantartas.save()

    return redirect('lapok.kezdolap')
