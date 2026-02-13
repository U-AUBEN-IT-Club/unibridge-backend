# Tests unitaires sur le module université.

from django.test import TestCase
from django.db import IntegrityError

from apps.core.models import University


def create_university(name: str, abbreviation: str) -> University:
    return University.objects.create(
        name = name, abbreviation = abbreviation
    )


class UniversityModelTests(TestCase):
    
    # Permet de détecter si les valeurs par défaut sont changées (accidentellement ou non)
    def test_create_university(self):
        """
        TEST: Les valeurs par défauts sont bien appliquées lorsqu'un étudiant est créé.
        """
        expected_name = "Univ"
        expected_abbreviation = "uv"

        university = create_university(
            name=expected_name,
            abbreviation=expected_abbreviation
        )
        
        self.assertEqual(university.name, expected_name)
        self.assertEqual(university.abbreviation, expected_abbreviation)
        self.assertIsNotNone(university.location)
        self.assertIsNotNone(university.joined_at)
    
    def test_unique_name(self):
        """
        TEST: Deux universités ne peuvent pas avoir le même nom.
        """
        duplicated_name = "Université 1"
        create_university(name=duplicated_name, abbreviation="univ1")

        # Si 2 universités on le même nom l'erreur ne sera pas lancée.
        with self.assertRaises(IntegrityError):
            create_university(name=duplicated_name, abbreviation="univ2")
    
    def test_unique_abbreviation(self):
        """
        TEST: Deux universités ne peuvent pas avoir la même abbréviation.
        """
        duplicated_abbreviation = "univ1"
        create_university(name="Université 1", abbreviation=duplicated_abbreviation)

        with self.assertRaises(IntegrityError):
            create_university(
                name="Université 2",
                abbreviation=duplicated_abbreviation
            )
    
    def test_str_representation(self):
        """
        TEST: str(université) retourne l'abréviation pour une université.
        """
        expected_abbreviation = "univ1"
        univ1 = create_university(
            name="Université 1",
            abbreviation=expected_abbreviation
        )

        self.assertEqual(str(univ1), expected_abbreviation)
