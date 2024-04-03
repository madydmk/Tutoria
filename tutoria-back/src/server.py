from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
# Définir le port à utiliser pour le serveur Flask
port = os.environ.get('FLASK_RUN_PORT', 5000)

@app.route('/')
def index():
    return 'Hello, World!'


def get_data():
    # Récupérer des données depuis la base de données ou d'autres sources
    data = {"message": "Données provenant du backend Flask"}
    return jsonify(data)

# Connexion
@app.route('/signIn')
def connect():
    data = {"message": "Données provenant du backend Flask"}
    return jsonify(data)

# Inscription
@app.route('/signUp')
def newAccount():
    data = {"message": "Données provenant du backend Flask"}
    return jsonify(data)

# Deconnexion
@app.route('/signOut')
def signeOut():
    data = {"message": "Données provenant du backend Flask"}
    return jsonify(data)



app.run(port=port)