import os
from django.core.wsgi import get_wsgi_application

"""
CONFIGURATION WSGI (Web Server Gateway Interface)
Ce fichier est le pont entre Django et le serveur Web (Production).
C'est ce qui permet au site d'être accessible sur internet.
"""

# Définit quel fichier de réglages utiliser (ici config/settings.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Crée l'objet 'application' que le serveur web va utiliser pour lancer le projet
application = get_wsgi_application()