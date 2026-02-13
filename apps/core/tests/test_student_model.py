# Tests unitaires sur le module étudiant.

from django.test import TestCase
from django.db import IntegrityError

from apps.core.models import University, Student


def create_university(name: str, abbreviation: str) -> University:
    return University.objects.create(
        name=name, abbreviation=abbreviation
    )

def create_student(
        first_name: str,
        last_name: str,
        email: str,
        university: University,
        filiere: str = "GL",
        level: int = 1
) -> Student:
    return Student.objects.create(
        first_name=first_name, last_name=last_name,
        email=email, university=university,
        filiere=filiere, level=level
    )


class StudentModelTests(TestCase):

    # Définis une université par défaut pour tous les étudiants qui seront
    # créés pour les tests.
    def setUp(self):
        self.university = create_university("Université 1", "univ1")
    
    def test_create_student(self):
        """
        TEST: Un étudiant peut être créé avec des informations de bases.
        """
        expected_email = "example@example.com"
        expected_last_name = "étudiant"
        expected_first_name = "226"

        student = create_student(
            first_name=expected_first_name,
            last_name=expected_last_name,
            email=expected_email,
            university=self.university
        )

        self.assertEqual(student.first_name, expected_first_name)
        self.assertEqual(student.last_name, expected_last_name)
        self.assertEqual(student.email, expected_email)
    
    def test_unique_email(self):
        """
        TEST: Deux étudiants ne peuvent pas avoir le même mail
        """
        duplicated_email = "example@example.com"
        create_student(
            first_name="étudiant", last_name="226",
            email=duplicated_email, university=self.university
        )

        with self.assertRaises(IntegrityError):
            create_student(
                first_name="étudiant2", last_name="226",
                email=duplicated_email, university=self.university
            )
    
    # Permet de détecter si les valeurs par défaut sont changées (accidentellement ou non)
    def test_default_value(self):
        """
        TEST: Les valeurs par défauts sont bien appliquées lorsqu'un étudiant est créé.
        """
        student = create_student(
            first_name="étudiant", last_name="226",
            email="example@example.com", university=self.university
        )

        self.assertEqual(student.filiere, "GL")
        self.assertEqual(student.level, 1)

    def test_university_student_number(self):
        """
        TEST: Le nombre d'étudiants d'une université change lorsqu'on en créé un.
        """
        create_student(
            first_name="étudiant", last_name="226",
            email="example@example.com", university=self.university
        )

        self.assertEqual(self.university.students.count(), 1)

    def test_cascade_deletion(self):
        """
        TEST: La supression d'une université supprime tous ces étudiants.
        """
        create_student(
            first_name="étudiant1", last_name="226",
            email="example@example.com", university=self.university
        )
        create_student(
            first_name="étudiant2", last_name="226",
            email="example2@example.com", university=self.university
        )

        self.university.delete()
        self.assertEqual(Student.objects.count(), 0)

    def test_get_filiere_display(self):
        """
        TEST: get_filiere_display affiche le nom complet d'une filière.
        """
        student = create_student(
            first_name="étudiant", last_name="226", email="example@example.com",
            university=self.university, filiere="RIT"
        )

        self.assertEqual(
            student.get_filiere_display(),
            "Réseaux et Informatique de Gestion"
        )

    def test_str_representation(self):
        """
        TEST: str(étudiant) retourne correctement les données de l'étudiant cible.
        """
        student = create_student(
            first_name="étudiant", last_name="226",
            email="example@example.com", university=self.university,
            filiere="GL", level=3
        )
        expected_resume = "étudiant 226 | Génie Logiciel (univ1)"

        self.assertEqual(str(student), expected_resume)