from django.shortcuts import render, redirect
from django.utils import timezone
from Kezdolap.models import Nyilvantartas

def kezdolap(request):
    nyilvantartas = Nyilvantartas.objects.all().order_by('visszaadva', '-datum')  # rendezés a vissza nem adaottak alapján
    kiadott_kulcsok_szama = nyilvantartas.filter(visszaadva__isnull=True).count()

    return render(request, 'index.html', {
            "nyilvantartas": nyilvantartas,
            "kiadott_kulcsok_szama": kiadott_kulcsok_szama,
        })

def mentes(request):
    if request.method == "POST":
        vezetek_nev = request.POST.get('vezetek_nev')
        kereszt_nev = request.POST.get('kereszt_nev')
        kulcs_szam = request.POST.get('kulcs_szam')

        # Ellenőrzés
        if vezetek_nev and kereszt_nev and kulcs_szam:
            # Új objektum és mentés
            Nyilvantartas.objects.create(vezetek_nev=vezetek_nev, kereszt_nev=kereszt_nev, kulcs_szam=kulcs_szam)

    return redirect('kezdolap')
def visszaadva(request, nyilvantartas_id):
    nyilvantartas = Nyilvantartas.objects.get(pk=nyilvantartas_id)
    nyilvantartas.visszaadva = timezone.now()  # aktuális időpont
    nyilvantartas.save()
    return redirect('kezdolap')  # Visszairányítjuk a főoldalra
