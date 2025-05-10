# Importation des librairies
from flask import Flask, jsonify, request
from google.cloud import storage
from datetime import datetime
import os
import csv
import io
from vertex_utils import generate_joke_with_vertex_ai  # Importe ta fonction

# Variables de configuration
GCS_BUCKET_NAME = "mini-api-python-bucket"
GCS_FILE_NAME = "data.csv"

# Initialiser le client GCS 
storage_client = storage.Client()

#Fonctions GCS
#Lecture
def read_csv_from_gcs():
    bucket = storage_client.bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(GCS_FILE_NAME)

      # Vérifie si le fichier existe
    if not blob.exists():
        return []  # Renvoie une liste vide si le fichier n'existe pas encore
    
    content = blob.download_as_text()
    reader = csv.DictReader(io.StringIO(content))
    return list(reader)

#Écriture / Insertion
def append_row_to_csv_in_gcs(new_data):
    bucket = storage_client.bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(GCS_FILE_NAME)

    rows = []
    fieldnames = list(new_data.keys())

    # Si le fichier existe, on le lit
    if blob.exists():
        content = blob.download_as_text()
        reader = csv.DictReader(io.StringIO(content))
        rows = list(reader)
        fieldnames = reader.fieldnames or fieldnames

    # Ajouter la nouvelle ligne
    rows.append(new_data)

    # Réécriture du fichier complet
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

    blob.upload_from_string(output.getvalue(), content_type="text/csv")


# Endpoints Flask
app = Flask(__name__)
app.debug = True

@app.route("/hello")
def hello():
    return jsonify({"message": "Bienvenue dans le mini API Python !"})

@app.route("/status")
def status():
    return jsonify({"server_time": datetime.now().isoformat()})


@app.route("/data", methods=["GET"])
def get_data():
    try:
        data = read_csv_from_gcs()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/data", methods=["POST"])
def post_data():
    try:
        new_data = request.get_json()
        append_row_to_csv_in_gcs(new_data)
        return jsonify({"message": "Ligne ajoutée"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/joke', methods=['GET'])
def joke():
    joke = generate_joke_with_vertex_ai()  # Appelle ta fonction
    if joke:
        return jsonify({"joke": joke})
    else:
        return jsonify({"error": "Erreur lors de la génération de la blague"}), 500



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

