from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    partner_verify_account_enabled = fields.Boolean(
        related='company_id.partner_verify_account_enabled',
        readonly=False,
        string='Require Verified Partner Before Posting Invoices/Bills',
    )
