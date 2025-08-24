FROM python:3.10

# Installer ffmpeg
RUN apt update && apt install -y ffmpeg

# Créer dossier de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY . .

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Point d’entrée : RunPod exécutera handler.py > handler(event)
CMD ["python3"]
