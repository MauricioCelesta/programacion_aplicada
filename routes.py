from resources import *
class AdminRutas:
    def init_rutas(self, aplicacion):
        aplicacion.add_resource(Primer_Recurso, '/primero')
        aplicacion.add_resource(SegundoRecurso, '/segundo')
        aplicacion.add_resource(Pagina1, '/')
        aplicacion.add_resource(BanjoTooie, '/faq')
        aplicacion.add_resource(Login, '/login')