# On utilise l'image Python 3.12.1
FROM python:3.12.1

# On définit le répertoire de travail dans l'image
WORKDIR /projet-13

# On copie les fichiers nécessaires du projet dans l'image
COPY . /projet-13

# On installe les dépendances du projet
RUN pip install -r requirements.txt

# On collecte les fichiers statiques
RUN python manage.py collectstatic --noinput

# On expose le port sur lequel l'application écoute
EXPOSE 8000

# On définit la commande par défaut pour exécuter l'application Django
CMD python manage.py runserver 0.0.0.0:8000