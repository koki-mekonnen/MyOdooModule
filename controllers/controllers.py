# -*- coding: utf-8 -*-
# from odoo import http


# class OdooFreelance(http.Controller):
#     @http.route('/odoo__freelance/odoo__freelance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo__freelance/odoo__freelance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo__freelance.listing', {
#             'root': '/odoo__freelance/odoo__freelance',
#             'objects': http.request.env['odoo__freelance.odoo__freelance'].search([]),
#         })

#     @http.route('/odoo__freelance/odoo__freelance/objects/<model("odoo__freelance.odoo__freelance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo__freelance.object', {
#             'object': obj
#         })

