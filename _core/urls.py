
from django.contrib import admin
from django.urls import path
from _core import views

urlpatterns = [
    path('', views.kezdolap, name='kezdolap'),
    path('admin/', admin.site.urls, name='admin'),
    path('visszaadva/<int:nyilvantartas_id>/', views.visszaadva, name='visszaadva'),
    path('mentes/', views.mentes, name='mentes'),

]
