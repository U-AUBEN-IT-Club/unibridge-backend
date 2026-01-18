from rest_framework import viewsets # Importation du moteur de vues de DRF
from rest_framework.permissions import AllowAny # permet de donnez acces a une vue a tous les utilisateurs
from .models import University, Student # Nos modèles (Database)
from .serializers import UniversitySerializer, StudentSerializer # Nos traducteurs JSON

"""
LOGIQUE DES VIEWS (CONTRÔLEURS) :
Nous utilisons les 'ModelViewSet' de Django REST Framework. 
Cette classe génère automatiquement toutes les actions CRUD standards :
- LIST (GET) : Récupérer tous les éléments
- CREATE (POST) : Ajouter un élément
- RETRIEVE (GET + ID) : Voir un élément précis
- UPDATE (PUT/PATCH + ID) : Modifier
- DELETE (DELETE + ID) : Supprimer

Si vous n'êtes pas famillier avec ces notions, je vous recommande de prendre le temps d'en apprendre plus avant de continuer
"""

class UniversityViewSet(viewsets.ModelViewSet):
    """
    ENDPOINT : /api/universities/
    USAGE FRONTEND : 
    - Pour afficher la liste des université par exemple.
    - Accès : GET pour lister, POST pour enregistrer une nouvelle école partenaire.
    """
    queryset = University.objects.all().order_by('abbreviation')
    serializer_class = UniversitySerializer
    permission_classes = [AllowAny]

class StudentViewSet(viewsets.ModelViewSet):
    """
    ENDPOINT : /api/students/
    USAGE FRONTEND : 
    - Note : On peut filtrer ou rechercher un étudiant par son ID via /api/students/{id}/
    - Le Front doit envoyer les données au format JSON correspondant aux champs du Serializer.
    """
    queryset = Student.objects.all().order_by('last_name')
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]