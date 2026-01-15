from django.apps import AppConfig

"""
CONFIGURATION DE L'APPLICATION
C'est ici que Django enregistre l'application 'core' et ses paramètres.
"""

class CoreConfig(AppConfig):
    # Important : On précise le chemin complet car l'app est dans le dossier 'apps'
    name = 'apps.core'