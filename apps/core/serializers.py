from rest_framework import serializers
from .models import University, Student

"""
LOGIQUE DES SERIALIZERS :
Les serializers servent de "traducteurs" entre les objets Python (modèles) 
et le format JSON utilisé par le Frontend. Ils gèrent aussi la validation 
des données entrantes (POST/PUT).
"""

class UniversitySerializer(serializers.ModelSerializer):
    """
    Transforme les données des universités.
    Utilisé pour lister les écoles dans les formulaires d'inscription.
    """
    class Meta:
        model = University
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    """
    Gère les profils étudiants.
    Note : 'university_details' est une lecture seule pour afficher 
    le nom de l'école au lieu de son simple ID technique.
    """
    university_details = UniversitySerializer(source='university', read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'university', 'university_details', 'filiere', 'level']