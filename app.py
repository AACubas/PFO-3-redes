from flask import Flask
from db import init_db
from routes import register_routes

app = Flask(__name__)
app.secret_key = "clave_secreta"

# Inicializar la base de datos
init_db()

# Registra las rutas
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
