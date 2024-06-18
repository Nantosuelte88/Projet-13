Procédures de déploiement et de gestion de l'application
=========================================================

Déploiement
-----------

Pour le déploiement de cette application, nous utilisons le service Render. Pour plus de détails à ce sujet, veuillez consulter sa documentation.

Étapes préliminaires
~~~~~~~~~~~~~~~~~~~~

1. Créez un compte sur `Docker <https://hub.docker.com/>`_ et sur `Render <https://dashboard.render.com/>`_.

2. Dans le projet GitHub, créez les variables suivantes (Settings -> Secrets and variables -> New repository secret):
   
   - DOCKERHUB_EMAIL
   - DOCKERHUB_PASSWORD
   - DOCKERHUB_USERNAME
   - RENDER_API_KEY (disponible dans vos paramètres sur le site Render -> API Keys -> Create API Key)
   - SECRET_KEY (qui est la clé secrète de votre application Django)


Création de l'image Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Accédez au fichier ``pipeline.yml`` et supprimez la partie "deploy to render" (attention sauvegardez-la dans un fichier texte).

2. Effectuez un commit avec cette modification pour déclencher automatiquement la pipeline.

3. Votre image Docker sera créée avec succès !


Déploiement sur Render
~~~~~~~~~~~~~~~~~~~~~~

1. Connectez-vous au site `Render <https://dashboard.render.com/>`_ et sélectionnez "New Web Service".

2. Choisissez l'option "Deploy an existing image from a registry".

3. Accédez à `DockerHub <https://hub.docker.com/>`_ et sélectionnez le nom de l'image précédemment créée (par exemple, "votrepseudo/nom-image:fjsdi475gfd54gf").

4. Revenez sur Render et saisissez ce nom dans le champ "Image URL".

5. Choisissez la région et le tarif adaptés à vos besoins. (la version gratuite fonctionne)

6. Appuyez sur "Create Web Service" (le déploiement peut prendre un peu de temps).


Configuration sur Render
~~~~~~~~~~~~~~~~~~~~~~~~

1. Dans les paramètres Render de votre service, accédez à Settings -> Deploy -> Docker Command et ajoutez la commande suivante : ``python manage.py runserver 0.0.0.0:8000``.

2. Rendez-vous dans Environment -> Environment Variables et ajoutez les variables suivantes :
   
   - SENTRY_DSN (adresse fournie par votre compte Sentry pour un suivi Sentry, facultatif)
   - DJANGO_ALLOWED_HOSTS (adresse de votre site sans "https://", par exemple "nom-image.onrender.com")

3. Une fois les mises à jour prises en compte, accédez à l'adresse de votre site (par exemple, "https://nom-image.onrender.com").


Intégration avec GitHub
~~~~~~~~~~~~~~~~~~~~~~~~

1. Dans Render, sélectionnez le nom de votre service (sous "Web Service", par exemple "nom-image:fjsdi475gfd54gf") et accédez aux variables GitHub.

2. Enregistrez le nom du service dans la variable "RENDER_SERVICE_NAME".

3. Réintégrez la partie "deploy to render" dans le fichier ``pipeline.yml``.

4. Effectuez un commit. En cas de problème, vérifiez vos variables d'environnement GitHub et Render, ou consultez les documentations.


Pipeline de déploiement
~~~~~~~~~~~~~~~~~~~~~~~~

Maintenant, les modifications apportées à votre code seront vérifiées dans la pipeline. Des tests seront effectués (vous pouvez en ajouter), la couverture de test (80% minimum) et le respect de la syntaxe (flake8) seront également vérifiés avant la création de l'image Docker et le déploiement.

Note : Seules les modifications effectuées sur la branche principale (main/master) déclencheront la création de l'image Docker et son déploiement.

N'hésitez pas à ajuster le formatage selon vos besoins et à ajouter des sections supplémentaires si nécessaire.
