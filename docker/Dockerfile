# Utiliser une image Python comme base
FROM python:3.13.1

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY flasktest.py /app
COPY requirements.txt /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000
EXPOSE 5000

# Commande pour démarrer l'application Flask
CMD ["python", "flasktest.py"]
