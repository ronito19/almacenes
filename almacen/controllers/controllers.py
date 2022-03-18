# -*- coding: utf-8 -*-
# from odoo import http


# class Almacen(http.Controller):
#     @http.route('/almacen/almacen/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almacen/almacen/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('almacen.listing', {
#             'root': '/almacen/almacen',
#             'objects': http.request.env['almacen.almacen'].search([]),
#         })

#     @http.route('/almacen/almacen/objects/<model("almacen.almacen"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almacen.object', {
#             'object': obj
#         })
