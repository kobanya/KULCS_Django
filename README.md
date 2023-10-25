# KULCS nyilvántartás
![Alt szöveg](https://github.com/kobanya/KULCS_Django/blob/master/static/kepernyo.png)

# Django - telepítés lépései
<li> A Django keretrendszer telepítése :  pip install django
 <li>  Virtuális környezet létrehozása: python3 -m venv .  (a pont ne maradjon el)
<li> Projekt létrehozása:  django-admin startproject Django  (a projekt neve)
<li> Tesztszerver indítása :  python3 manage.py runserver
<li> Ne feledd el leállítani :  CTRL + C
<li> Az adatbázis előkészítése:  python3 manage.py makemigrations
<li> Az adatbázis betöltése: python3 manage.py migrate
<li> Administrator létrehozása:    python3 manage.py createsuperuser
<li> Bejelentkezéshez az admin felületre a böngészőbe a következőt írjátok: localhost:8000/admin
<li> QR beolvasásos kulcskiadás

![Alt szöveg](https://github.com/kobanya/KULCS_Django/blob/master/static/QR_olvasas.gif)
