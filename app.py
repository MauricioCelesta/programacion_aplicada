from flask import Flask
from flask_restful import Api
from routes import AdminRutas
# importamos las librerías y clases necesarias

app = Flask(__name__)
# creamos nuestro servidor y lo guardamos en la variable app
api = Api(app)
# creamos el motor que hace funcionar el servidor y lo guardamos en la variable api
rutas = AdminRutas()
# objeto que controla todas mis rutas
rutas.init_rutas(api)
# ponemos a correr el servidor y lo ponemos en modo debug y en el puerto 8000
app.run(debug=True, port=8000)