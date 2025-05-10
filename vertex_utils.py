from flask import Flask, jsonify
from vertexai.preview.generative_models import GenerativeModel, ChatSession
import vertexai
import os

def generate_joke_with_vertex_ai():
    try:
        # Récupérer les variables d'environnement
        project = os.getenv("GCP_PROJECT")
        location = os.getenv("GCP_REGION", "us-central1")  # Ou une autre région si nécessaire

        # Initialiser Vertex AI
        vertexai.init(project=project, location=location)

        # Utiliser le modèle Gemini-2.0-flash-001
        model = GenerativeModel(model_name="gemini-2.0-flash-001")

        # Démarrer une session de chat
        chat: ChatSession = model.start_chat()

        # Définir le prompt pour générer une blague
        questions = [
            "Salut ! Raconte-moi une blague courte et drôle en français.",
        ]

        joke = ""
        for q in questions:
            response = chat.send_message(q)
            joke = response.text.strip()  # Capturer la blague générée

        return joke  # Retourner la blague générée

    except Exception as e:
        # Afficher l'erreur détaillée pour mieux comprendre
        print(f"Erreur lors de la génération de texte : {e}")
        return f"Erreur lors de la génération de la blague : {str(e)}"

# Exemple d'appel :
if __name__ == "__main__":
    generate_joke_with_vertex_ai()
