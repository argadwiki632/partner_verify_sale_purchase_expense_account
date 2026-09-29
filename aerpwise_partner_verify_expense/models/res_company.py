from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    partner_verify_expense_enabled = fields.Boolean(
        string='Require Verified Partners on Expenses',
        default=False,
        help=(
            'If enabled, expense reports cannot be submitted or approved '
            'unless the employee work contact and any expense vendors '
            'are verified.'
        ),
    )
