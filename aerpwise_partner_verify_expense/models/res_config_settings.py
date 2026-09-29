from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    partner_verify_expense_enabled = fields.Boolean(
        related='company_id.partner_verify_expense_enabled',
        readonly=False,
        string='Require Verified Partners Before Expense Submit/Approve',
    )
