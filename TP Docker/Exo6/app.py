from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

@app.route("/")
def index():
    try:
        # fabriquer l'URL Mongo avec les variables d'env
        mongo_url = os.environ.get("MONGO_URL", "mongodb://db:27017/")
        client = MongoClient(mongo_url)
        db = client.test_database
        server_status = db.command("serverStatus")
        return "Connexion MongoDB réussie !"
    except Exception as e:
        return f"Erreur de connexion à MongoDB: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
