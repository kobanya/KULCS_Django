from django.db import models

class Nyilvantartas(models.Model):
    vezetek_nev = models.CharField(max_length=30)
    kereszt_nev = models.CharField(max_length=30)
    kulcs_szam = models.CharField(max_length=15)
    datum = models.DateTimeField(auto_now_add=True)
    visszaadva = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.vezetek_nev}  {self.kereszt_nev} - {self.kulcs_szam}"