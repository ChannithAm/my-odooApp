# -*- coding: utf-8 -*-
from odoo import http

# class Openclass(http.Controller):
#     @http.route('/openclass/openclass/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openclass/openclass/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openclass.listing', {
#             'root': '/openclass/openclass',
#             'objects': http.request.env['openclass.openclass'].search([]),
#         })

#     @http.route('/openclass/openclass/objects/<model("openclass.openclass"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openclass.object', {
#             'object': obj
#         })