# Image de base officielle Python
FROM python:3.11-slim

# Dossier de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exposer le port 8080 (Cloud Run utilisera ce port)
EXPOSE 8080

# Lancer l'application avec le bon port Cloud Run
CMD ["python", "app.py"]
