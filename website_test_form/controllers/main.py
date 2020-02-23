# Copyright 2019 Kevin Kamau
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import http
from odoo.http import request

# used to verify the key
SITE_VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'


class WebsiteTestController(http.Controller):

    @http.route('/test_form', type="http", auth="public",
                website=True)
    def test_form(self):
        # Get the site key
        key = request.env['ir.config_parameter'].sudo().get_param(
                'website_recaptcha_v2.recaptcha_website_site_key')
        # set/render site key to the form div
        return request.render('website_test_form.website_form_test',
                              {'site_key': key})
