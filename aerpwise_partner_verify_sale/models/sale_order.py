from odoo import models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _confirmation_error_message(self):
        message = super()._confirmation_error_message()
        if message:
            return message

        if not self.company_id.partner_verify_sale_enabled:
            return False

        partner = self.partner_id.commercial_partner_id
        if partner.partner_verify_state != 'verified':
            return _(
                'Sales Order cannot be confirmed because customer '
                '%(partner)s is not verified (status: %(status)s).'
            ) % {
                'partner': partner.display_name,
                'status': partner._get_partner_verify_status_label(),
            }

        return False
