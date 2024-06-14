Instructions d'installation
============================

Pour installer le projet, suivez les étapes ci-dessous :

1. Cloner ou télécharger le repository
   .. code-block:: sh

        git clone https://github.com/Nantosuelte88/Projet-13.git (ou "Download ZIP")

2. Créer l'environnement virtuel
   .. code-block:: sh

        python -m venv venv

3. Activer l'environnement sur Unix et MacOS
   .. code-block:: sh

        source venv/bin/activate

4. Pour l'activer sur Windows (Pas de ".bat" sous Powershell)
   .. code-block:: sh

        venv\Scripts\activate.bat

5. Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure
   .. code-block:: sh
        python --version

6. Confirmer que la commande pip exécute l'exécutable pip dans l'environnement virtuel
   .. code-block:: sh

        pip --version

 Pour désactiver l'environnement
   .. code-block:: sh

        deactivate


Pour installer les requirements : 

8. Activez l'environnement virtuel
   .. code-block:: sh

        source venv/bin/activate

9. Installez les dépendances du projet en exécutant
   .. code-block:: sh

        pip install --requirement requirements.txt
