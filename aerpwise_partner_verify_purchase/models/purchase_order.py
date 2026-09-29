from odoo import models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        for order in self:
            if not order.company_id.partner_verify_purchase_enabled:
                continue
            order.partner_id._raise_if_unverified(_(
                'Purchase Order cannot be confirmed because vendor '
                '%(partner)s is not verified (status: %(status)s).'
            ))
        return super().button_confirm()
