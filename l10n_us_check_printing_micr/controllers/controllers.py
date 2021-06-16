# -*- coding: utf-8 -*-
# from odoo import http


# class L10nUsCheckPrintingMicr(http.Controller):
#     @http.route('/l10n_us_check_printing_micr/l10n_us_check_printing_micr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_us_check_printing_micr/l10n_us_check_printing_micr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_us_check_printing_micr.listing', {
#             'root': '/l10n_us_check_printing_micr/l10n_us_check_printing_micr',
#             'objects': http.request.env['l10n_us_check_printing_micr.l10n_us_check_printing_micr'].search([]),
#         })

#     @http.route('/l10n_us_check_printing_micr/l10n_us_check_printing_micr/objects/<model("l10n_us_check_printing_micr.l10n_us_check_printing_micr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_us_check_printing_micr.object', {
#             'object': obj
#         })
