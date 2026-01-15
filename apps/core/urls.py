from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UniversityViewSet, StudentViewSet

"""
CONFIGURATION DES ROUTES (URLS)
Le Router de Django REST Framework génère automatiquement les adresses (endpoints)
pour notre API. Pas besoin de créer chaque URL (GET, POST, etc.) à la main.
"""

# Initialisation du routeur automatique
router = DefaultRouter()

# Enregistrement des ressources (modèles) accessibles via l'API
# /api/universities/ -> gère toutes les actions sur les universités
router.register(r'universities', UniversityViewSet)

# /api/students/ -> gère toutes les actions sur les étudiants
router.register(r'students', StudentViewSet)

"""
Logique d'accès pour le Frontend :
- GET /api/students/ : Récupère la liste de tous les membres.
- POST /api/students/ : Enregistre un nouveau membre.
- GET /api/students/1/ : Récupère les détails du membre avec l'ID 1.
"""

# On inclut toutes les routes générées par le router dans les URLs de l'app
urlpatterns = [
    path('', include(router.urls)),
]