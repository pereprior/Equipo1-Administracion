# -*- coding: utf-8 -*-
# from odoo import http


# class Feeljoy(http.Controller):
#     @http.route('/feeljoy/feeljoy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feeljoy/feeljoy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('feeljoy.listing', {
#             'root': '/feeljoy/feeljoy',
#             'objects': http.request.env['feeljoy.feeljoy'].search([]),
#         })

#     @http.route('/feeljoy/feeljoy/objects/<model("feeljoy.feeljoy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feeljoy.object', {
#             'object': obj
#         })
