from django.db import models

class Nyilvantartas(models.Model):
    vezetek_nev = models.CharField(max_length=30)
    kereszt_nev = models.CharField(max_length=30)
    kulcs_szama = models.CharField(max_length=10)
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vezetek_nev} {self.kereszt_nev}"
