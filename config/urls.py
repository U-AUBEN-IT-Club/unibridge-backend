from django.contrib import admin
from django.urls import path, include

"""
CONFIGURATION GLOBALE DES URLS
Ce fichier est le point d'entrée principal. Il redirige les requêtes 
vers l'administration ou vers les différentes applications du projet.
"""

urlpatterns = [
    # Interface de gestion visuelle (Back-office)
    path('admin/', admin.site.urls),
    
    # Point d'entrée de l'API : toutes les routes de l'application 'core'
    # seront accessibles via le préfixe http://127.0.0.1:8000/api/
    path('api/', include('apps.core.urls')),
]