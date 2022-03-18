# -*- coding: utf-8 -*-
# from odoo import http


# class Envios(http.Controller):
#     @http.route('/envios/envios/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/envios/envios/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('envios.listing', {
#             'root': '/envios/envios',
#             'objects': http.request.env['envios.envios'].search([]),
#         })

#     @http.route('/envios/envios/objects/<model("envios.envios"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('envios.object', {
#             'object': obj
#         })
