from django.contrib import admin
from django.urls import path
from layanglayang.views import indexlayanglayang
from Persegi.views import indexpersegi
from persegipanjang.views import indexpersegipanjang
from Trapesium.views import indextrapesium
from Profil.views import indexprofil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('layanglayang/', indexlayanglayang),
    path('Persegi/', indexpersegi),
    path('persegipanjang/', indexpersegipanjang),
    path('Trapesium/', indextrapesium),
    path('Profil/', indexprofil),
]
