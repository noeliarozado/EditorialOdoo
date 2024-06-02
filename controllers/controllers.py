# -*- coding: utf-8 -*-
# from odoo import http


# class Editorial(http.Controller):
#     @http.route('/editorial/editorial', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/editorial/editorial/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('editorial.listing', {
#             'root': '/editorial/editorial',
#             'objects': http.request.env['editorial.editorial'].search([]),
#         })

#     @http.route('/editorial/editorial/objects/<model("editorial.editorial"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('editorial.object', {
#             'object': obj
#         })
