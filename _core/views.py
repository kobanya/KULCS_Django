from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages  # Hibaüzenetekhez

from Kezdolap.models import Nyilvantartas, Kulcs

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
            try:
                # Próbálj meg lekérdezni egy olyan kulcsot az adatbázisból, amelynek a mennyisége nagyobb, mint 0 és megfelelő kulcsszámmal rendelkezik.
                kulcs_obj = Kulcs.objects.get(kulcs_szam=kulcs_szam, mennyiseg__gt=0)
            except Kulcs.DoesNotExist:
                messages.error(request, "A megadott kulcs nem érhető el.")
            else:
                Nyilvantartas.objects.create(vezetek_nev=vezetek_nev, kereszt_nev=kereszt_nev, kulcs_szam=kulcs_szam)
                # Csökkentsd a rendelkezésre álló kulcsok mennyiségét
                kulcs_obj.mennyiseg -= 1
                kulcs_obj.save()
        else:
            messages.error(request, "Hiányzó adatok. Töltse ki az összes mezőt.")

    return redirect('kezdolap')

def visszaadva(request, nyilvantartas_id):
    nyilvantartas = Nyilvantartas.objects.get(pk=nyilvantartas_id)
    nyilvantartas.visszaadva = timezone.now()  # aktuális időpont
    nyilvantartas.save()
    # Növeld a rendelkezésre álló kulcsok mennyiségét
    kulcs_obj = Kulcs.objects.first()  # Első kulcs objektum
    kulcs_obj.mennyiseg += 1
    kulcs_obj.save()
    return redirect('kezdolap')
