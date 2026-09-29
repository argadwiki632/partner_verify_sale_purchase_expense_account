from odoo import models, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _post(self, soft=True):
        for move in self:
            if not move.company_id.partner_verify_account_enabled:
                continue
            if not move.is_invoice(include_receipts=True):
                continue
            if not move.partner_id:
                continue
            move.partner_id._raise_if_unverified(_(
                'Journal entry cannot be posted because partner '
                '%(partner)s is not verified (status: %(status)s).'
            ))
        return super()._post(soft=soft)
