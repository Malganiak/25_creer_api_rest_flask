from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Paramètres de connexion à la base de données
host = "localhost"
user = "root"
password = "toor"
database = "films_database"
table_name = "films"

# Route pour récupérer la liste des films
@app.route('/films', methods=['GET'])
def get_films():
    try:
        # Connexion à la base de données
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = connection.cursor(dictionary=True)

        # Exécution de la requête
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        films = cursor.fetchall()

        # Fermeture de la connexion à la base de données
        cursor.close()
        connection.close()

        # Retourne la liste des films au format JSON
        return jsonify(films)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
