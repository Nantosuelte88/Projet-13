Instructions d'installation
============================

Pour installer le projet, suivez les étapes ci-dessous :

.. code-block:: sh

    # Cloner ou télécharger le repository
    git clone https://github.com/Nantosuelte88/Projet-13.git (ou "Download ZIP")

    # Créer l'environnement virtuel
    python -m venv venv

    # Activer l'environnement sur Unix et MacOS
    source venv/bin/activate

    # Pour l'activer sur Windows (Pas de ".bat" sous Powershell)
    venv\Scripts\activate.bat

    # Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure
    python --version

    # Confirmer que la commande pip exécute l'exécutable pip dans l'environnement virtuel
    pip --version

    # Pour désactiver l'environnement
    deactivate

    # Activez l'environnement virtuel
    source venv/bin/activate

    # Installez les dépendances du projet en exécutant
    pip install --requirement requirements.txt
    