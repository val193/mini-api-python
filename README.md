# Mini API Python

Une API REST simple construite avec Flask qui permet de gérer des données et de générer des blagues en utilisant Google Cloud Platform.

## Fonctionnalités

- Endpoint `/hello` : Message de bienvenue
- Endpoint `/status` : Affiche l'heure du serveur
- Endpoint `/data` : 
  - GET : Récupère toutes les données stockées dans Google Cloud Storage
  - POST : Ajoute une nouvelle ligne de données
- Endpoint `/joke` : Génère une blague en utilisant Google Vertex AI (Gemini)

## Prérequis

- Python 3.x
- Un compte Google Cloud Platform
- Les variables d'environnement suivantes configurées :
  - `GCP_PROJECT` : ID de votre projet GCP
  - `GCP_REGION` : Région GCP (par défaut : us-central1)

## Installation

1. Cloner le repository :
```bash
git clone [https://github.com/val193/mini-api-python]
cd mini-api-python-1
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurer les variables d'environnement :
```bash
export GCP_PROJECT="mini-api-python"
export GCP_REGION="us-central1"
```

## Utilisation

1. Lancer l'application :
```bash
python app.py
```

L'API sera accessible sur `http://localhost:8080`

## Endpoints disponibles

### GET /hello
```bash
curl http://localhost:8080/hello
```

### GET /status
```bash
curl http://localhost:8080/status
```

### GET /data
```bash
curl http://localhost:8080/data
```

### POST /data
```bash
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://localhost:8080/data
```

### GET /joke
```bash
curl http://localhost:8080/joke
```

## Déploiement

Le projet inclut un `Dockerfile` pour le conteneurisation et un script `deploy.sh` pour le déploiement.

Pour construire et déployer :
```bash
./deploy.sh
```

## Structure du projet

- `app.py` : Application principale Flask
- `vertex_utils.py` : Utilitaires pour l'intégration avec Google Vertex AI
- `requirements.txt` : Dépendances Python
- `Dockerfile` : Configuration pour la conteneurisation
- `deploy.sh` : Script de déploiement

## Stockage des données

Les données sont stockées dans un bucket Google Cloud Storage (`mini-api-python-bucket`) au format CSV.

