from django.contrib import admin
from .models import University, Student

"""
CONFIGURATION DE L'ADMINISTRATION
Ce fichier permet d'activer l'interface visuelle pour gérer les données 
sans passer par des requêtes SQL ou l'API.
"""

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    """
    Configuration pour le modèle Université.
    - list_display : définit les colonnes visibles dans la liste.
    """
    list_display = ('abbreviation', 'name', 'joined_at')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Configuration pour le modèle Étudiant.
    - list_display : affiche les infos clés (Nom, Ecole, Filière).
    - list_filter : ajoute un menu à droite pour filtrer rapidement par Ecole ou Filière.
    """
    list_display = ('first_name', 'last_name', 'university', 'filiere', 'level')
    
    # Très utile pour isoler les étudiants d'une école précise lors d'une réunion
    list_filter = ('university', 'filiere')