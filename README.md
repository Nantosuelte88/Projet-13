## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement sur Unix et MacOS `source venv/bin/activate`
- Pour l'activer sur Windows (Pas de ".bat" sous Powershell) `env\Scripts\activate.bat`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `pip --version`
- Pour désactiver l'environnement, `deactivate`

#### Mise en place

- Activez l'environnement virtuel
- Installez les dépendances du projet en exécutant `pip install --requirement requirements.txt`
- Renommez le fichier "env" en ".env"
- Pour la valeur de "SENTRY_DSN=", trouvez le lien correspondant dans les paramètres de votre compte Sentry
- Pour la valeur de "SECRET_KEY=", exécutez `python create_secret_key.py` dans la console (vous pouvez supprimer le fichier après)
- Copiez la clé générée qui s'affiche dans la console
- Sauvegardez le fichier .env
- À la racine du projet, exécutez `python manage.py collecstatic`

#### Exécuter le site

- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `source venv/bin/activate`
- `pytest`

#### Base de données

- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`


## Déploiement

Pour le déploiement de cette application, nous utilisons le service Render. Pour plus de détails à ce sujet, veuillez consulter sa documentation.

### Étapes préliminaires

1. Créez un compte sur [Docker](https://hub.docker.com/) et sur [Render](https://dashboard.render.com/).

2. Dans le projet GitHub, créez les variables suivantes (Settings -> Secrets and variables -> New repository secret):

   - DOCKERHUB_EMAIL
   - DOCKERHUB_PASSWORD
   - DOCKERHUB_USERNAME
   - RENDER_API_KEY (disponible dans vos paramètres sur le site Render -> API Keys -> Create API Key)

### Création de l'image Docker

1. Accédez au fichier pipeline.yml et supprimez la partie "deploy to render" (attention sauvegardez-la dans un fichier texte).

2. Effectuez un commit avec cette modification pour déclencher automatiquement la pipeline.

3. Votre image Docker sera créée avec succès !

### Déploiement sur Render

1. Connectez-vous au site [Render](https://dashboard.render.com/) et sélectionnez "New Web Service".

2. Choisissez l'option "Deploy an existing image from a registry".

3. Accédez à [DockerHub](https://hub.docker.com/) et sélectionnez le nom de l'image précédemment créée (par exemple, "votrepseudo/nom-image:fjsdi475gfd54gf").

4. Revenez sur Render et saisissez ce nom dans le champ "Image URL".

5. Choisissez la région et le tarif adaptés à vos besoins. (la version gratuite fonctionne)

6. Appuyez sur "Create Web Service" (le déploiement peut prendre un peu de temps).

### Configuration sur Render

1. Dans les paramètres Render de votre service, accédez à Settings -> Deploy -> Docker Command et ajoutez la commande suivante : "python manage.py runserver 0.0.0.0:8000".

2. Rendez-vous dans Environment -> Environment Variables et ajoutez les variables suivantes :

   - SENTRY_DSN (adresse fournie par votre compte Sentry pour un suivi Sentry, facultatif)
   - DJANGO_ALLOWED_HOSTS (adresse de votre site sans "https://", par exemple "nom-image.onrender.com")

3. Une fois les mises à jour prises en compte, accédez à l'adresse de votre site (par exemple, "https://nom-image.onrender.com").

### Intégration avec GitHub

1. Dans Render, sélectionnez le nom de votre service (sous "Web Service", par exemple "nom-image:fjsdi475gfd54gf") et accédez aux variables GitHub.

2. Enregistrez le nom du service dans la variable "RENDER_SERVICE_NAME".

3. Réintégrez la partie "deploy to render" dans le fichier pipeline.yml.

4. Effectuez un commit. En cas de problème, vérifiez vos variables d'environnement GitHub et Render, ou consultez les documentations.

### Pipeline de déploiement

Maintenant, les modifications apportées à votre code seront vérifiées dans la pipeline. Des tests seront effectués (vous pouvez en ajouter), la couverture de test (80% minimum) et le respect de la syntaxe (flake8) seront également vérifiés avant la création de l'image Docker et le déploiement.

Note : Seules les modifications effectuées sur la branche principale (main/master) déclencheront la création de l'image Docker et son déploiement.
N'hésitez pas à ajuster le formatage selon vos besoins et à ajouter des sections supplémentaires si nécessaire.
