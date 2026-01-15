import os
from django.core.asgi import get_asgi_application

"""
CONFIGURATION ASGI (Asynchronous Server Gateway Interface)
Ce fichier est le point d'entrée pour les serveurs web modernes (Asynchrones).
Il permet de gérer :
1. Le trafic Web classique (HTTP)
2. Les protocoles en temps réel comme les WebSockets (Chat, Notifications)
"""

# Indique à Django quel fichier de paramètres utiliser
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Initialise l'application en mode asynchrone
application = get_asgi_application()