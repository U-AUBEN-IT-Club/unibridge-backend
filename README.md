# unibridge-backend

# Plateforme de Gestion Inter-Universitaire (Club Informatique) 🚀

Cette plateforme est un projet ouvert du club informatique en partenariat avec d'autres club  d'universités partenaires. Elle a pour but d'etre un projet collaboratif et permettre de creer un reseau de networking interuniversitaire.

## 🏗️ Architecture du Projet
Le projet est bâti sur une architecture **Django + Django REST Framework**, structurée de manière modulaire pour garantir la scalabilité et la maintenance.

* **Core App** : Gestion des universités et des profils étudiants.
* **API** : Interface RESTful standardisée pour le futur Frontend (React/Vue).
* **Admin** : Interface de gestion visuelle pour les responsables du club.

---

## 🛠️ Technologies Utilisées
* **Backend** : Python 3.12+ / Django 6.0.1
* **API** : Django REST Framework (DRF)
* **Base de données** : SQLite (Développement) / PostgreSQL (Production)
* **Serveur** : WSGI/ASGI pour la compatibilité temps réel.

---

## 🛠️🛠️ Contraintes de Développement (Règles de l'équipe)

Pour maintenir la qualité du code et la cohérence du projet, chaque contributeur doit respecter les règles suivantes :

1. **Structure des Applications** : 
   - Toutes les nouvelles applications Django doivent impérativement être créées dans le dossier `/apps/`.
   - Commande : `cd apps && python ../manage.py startapp nom_de_l_app`

2. **Gestion des Dépendances** :
   - Avant chaque `git commit`, si vous avez installé un nouveau package, vous devez mettre à jour le fichier des dépendances.
   - Commande : `pip freeze > requirements.txt`

3. **Documentation et Clarté** :
   - Chaque fonction, classe ou modèle doit être accompagné d'un commentaire expliquant son rôle.
   - Les commentaires doivent être simples et compréhensibles par tous les membres.

4. **Modifications du `settings.py`** :
   - Toute modification des paramètres globaux (Base de données, Clés API, Middlewares) doit être signalée par un commentaire explicite indiquant la raison du changement et l'auteur.

5. **Messages de Commit** :
   - Utilisez des messages explicites. 
   - *Exemple :* `Fix: Correction du bug d'inscription des étudiants` au lieu de `Modif`.

---

## 🚀 Installation Rapide

1. **Cloner le projet** :

    *Vous pouvez utilisez github desktop pour cette etape*

   ```bash
    
   git clone <url-du-depot>
   cd nom-du-projet


2. **Créer l'environnement virtuel** :
    ```Bash

    python -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate


3. **Installer les dépendances** :
    ```Bash

    pip install -r requirements.txt
    

4. **Lancer les migrations** :
    ```Bash

    python manage.py makemigrations
    python manage.py migrate


5. **Créer un compte Admin** :
    ```Bash

    python manage.py createsuperuser

6. **Lancer le serveur** :
    ```Bash
    python manage.py runserver