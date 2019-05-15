# -*- coding: utf-8 -*-
from odoo import http

# class MrpRunScheduler(http.Controller):
#     @http.route('/mrp_run_scheduler/mrp_run_scheduler/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrp_run_scheduler/mrp_run_scheduler/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrp_run_scheduler.listing', {
#             'root': '/mrp_run_scheduler/mrp_run_scheduler',
#             'objects': http.request.env['mrp_run_scheduler.mrp_run_scheduler'].search([]),
#         })

#     @http.route('/mrp_run_scheduler/mrp_run_scheduler/objects/<model("mrp_run_scheduler.mrp_run_scheduler"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrp_run_scheduler.object', {
#             'object': obj
#         })