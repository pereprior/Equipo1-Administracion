# -*- coding: utf-8 -*-
# from odoo import http


# class Gatos(http.Controller):
#     @http.route('/gatos/gatos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gatos/gatos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gatos.listing', {
#             'root': '/gatos/gatos',
#             'objects': http.request.env['gatos.gatos'].search([]),
#         })

#     @http.route('/gatos/gatos/objects/<model("gatos.gatos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gatos.object', {
#             'object': obj
#         })
