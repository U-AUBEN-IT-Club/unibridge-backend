from django.db import models

"""
ARCHITECTURE DES MODÈLES :
Ces classes définissent la structure de la base de données (Schéma).
Chaque modification ici nécessite une migration :
1. python manage.py makemigrations
2. python manage.py migrate
"""

class University(models.Model):
    """
    TABLE : University
    LOGIQUE : Répertorie les institutions partenaires. 
    L'abréviation est utilisée comme identifiant visuel unique.
    """
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=20, help_text="Ex: USTB, UJKZ, VESSA", unique=True)
    location = models.CharField(max_length=255, blank=True )
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Universities" # Correction de l'affichage dans l'admin

    def __str__(self):
        return self.abbreviation


class Student(models.Model):
    """
    TABLE : Student
    LOGIQUE : Profil individuel des membres. 
    RELATION : Chaque étudiant appartient à UNE SEULE université (Many-to-One).
    Si l'université est supprimée, les profils étudiants liés le sont aussi (CASCADE).
    """
    FILIERES = [
        ('GL', 'Génie Logiciel'),
        ('RIT', 'Réseaux et Informatique de Gestion'),
        ('MIAGE', 'Méthodes Informatiques Appliquées à la Gestion'),
        ('OTHER', 'Autre'),
    ]

    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(unique=True, verbose_name="Adresse Email")
    
    # Relation vers l'université : Permet de grouper les étudiants par école
    university = models.ForeignKey(
        University, 
        on_delete=models.CASCADE, 
        related_name='students'
    )
    
    filiere = models.CharField(
        max_length=10, 
        choices=FILIERES, 
        default='GL',
        verbose_name="Filière académique" 
    )
    
    level = models.IntegerField(
        help_text="Année d'étude actuelle (ex: 1 pour L1, 3 pour L3)", 
        default=1,
        verbose_name="Niveau"
    )
    
    """
        Verbose_name: À quoi ça sert ? Ça permet de donner un nom propre
        avec des accents et des majuscules, qui apparaîtra dans l'interface 
        d'administration et dans les messages d'erreur.
    """

    def __str__(self):
        # Affiche un résumé clair dans l'interface d'administration
        return f"{self.first_name} {self.last_name} | {self.get_filiere_display()} ({self.university.abbreviation})"