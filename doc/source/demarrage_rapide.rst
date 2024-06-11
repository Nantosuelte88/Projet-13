Guide de démarrage rapide
=========================

1. Renommez le fichier "env" en ".env"
   
2. Pour la valeur de "SENTRY_DSN=", trouvez le lien correspondant dans les paramètres de votre compte Sentry.

3. Pour la valeur de "SECRET_KEY=", exécutez la commande suivante dans la console :

   .. code-block:: sh

       python create_secret_key.py

   Vous pouvez supprimer le fichier après.

4. Copiez la clé générée qui s'affiche dans la console.

5. Sauvegardez le fichier .env.

6. À la racine du projet, exécutez :

   .. code-block:: sh

       python manage.py collectstatic

7. Vous pouvez désormais lancer le site avec la commande suivante :

   .. code-block:: sh

       python manage.py runserver

8. Aller sur `http://localhost:8000` dans un navigateur.
