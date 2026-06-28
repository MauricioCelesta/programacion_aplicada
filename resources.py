from flask_restful import Resource
from flask import render_template, make_response, request
# importamos las librerías y clases que ocupamos
class Primer_Recurso(Resource):
    def get(self):
        banjo_kazooie = [
        ["Mumbo's mountain", "Treasure Trove Cove", "Clanker's Cavern"],
        ["Bubblegloop swamp", "Freezeezy Peak", "Gobi's Valley"],
        ["Mad Monster Mansion", "Rusty Bucket Bay", "Click Clock Wood"]]
        return banjo_kazooie

# hacemos el segundo recurso
class SegundoRecurso(Resource):
    def get(self):
        banjo_tooie = {"Mundo 1": "Mayahem Temple", "Mundo 2": "Glitter Gulch Mine", "Mundo 3": "WitchyWorld", "mundo 4": "Jolly Roger's Lagoon", "mundo 5": "Terrydactyland", "mundo 6": "Grunty Industries", "mundo 7": "Hailfire Peaks", "mundo 8": "Cloud Cuckooland"}
        return banjo_tooie

# terminamos con el segundo recurso y vamos a renderizar páginas web

class Pagina1(Resource):
    def get(self):
        # renderizamos la página index
        sitio_web_renderizado = render_template('index.html')
        return make_response(sitio_web_renderizado)
# vamos a renderizar una segunda página, esta de banjo tooie

class BanjoTooie(Resource):
    def get(self):
        # renderizamos el sitio
        sitio_web_renderizado = render_template('banjo_tooie.html')
        return make_response(sitio_web_renderizado)

# añadimos la página de login
class Login(Resource):
    def get(self):
        sitio_web_renderizado = render_template('login.html')
        return make_response(sitio_web_renderizado)
    def post(self):
        info_usuario = request.form.get('email')
        password = request.form.get('password')
        return {'Correo electrónico': info_usuario, 'Contraseña': password}