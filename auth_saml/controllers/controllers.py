# -*- coding: utf-8 -*-
# from odoo import http


# class AuthSaml(http.Controller):
#     @http.route('/auth_saml/auth_saml/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/auth_saml/auth_saml/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('auth_saml.listing', {
#             'root': '/auth_saml/auth_saml',
#             'objects': http.request.env['auth_saml.auth_saml'].search([]),
#         })

#     @http.route('/auth_saml/auth_saml/objects/<model("auth_saml.auth_saml"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('auth_saml.object', {
#             'object': obj
#         })
