# -*- coding: utf-8 -*-
from odoo import http

# class TaxiManager(http.Controller):
#     @http.route('/taxi_manager/taxi_manager/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/taxi_manager/taxi_manager/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('taxi_manager.listing', {
#             'root': '/taxi_manager/taxi_manager',
#             'objects': http.request.env['taxi_manager.taxi_manager'].search([]),
#         })

#     @http.route('/taxi_manager/taxi_manager/objects/<model("taxi_manager.taxi_manager"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('taxi_manager.object', {
#             'object': obj
#         })