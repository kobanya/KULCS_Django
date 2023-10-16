from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from Kezdolap.models import Nyilvantartas

def kezdolap(request):
    nyilvantartas = Nyilvantartas.objects.all().order_by('visszaadva', 'datum')  # rendezés a vissza nem adaottak alapján
    return render(request, 'index.html', {"nyilvantartas": nyilvantartas})

def mentes(request):
    if request.method == "POST":
        vezetek_nev = request.POST.get('vezetek_nev')
        kereszt_nev = request.POST.get('kereszt_nev')
        kulcs_szam = request.POST.get('kulcs_szam')

        # Ellenőrizze, hogy az összes szükséges adat rendelkezésre áll
        if vezetek_nev and kereszt_nev and kulcs_szam:
            # Hozzon létre egy új objektumot és mentsen az adatbázisba
            Nyilvantartas.objects.create(vezetek_nev=vezetek_nev, kereszt_nev=kereszt_nev, kulcs_szam=kulcs_szam)

    # Visszairányítás a főoldalra
    return redirect('kezdolap')
def visszaadva(request, nyilvantartas_id):
    nyilvantartas = Nyilvantartas.objects.get(pk=nyilvantartas_id)
    nyilvantartas.visszaadva = timezone.now()  # Beállítjuk az aktuális időpontra
    nyilvantartas.save()
    return redirect('kezdolap')  # Visszairányítjuk a főoldalra
