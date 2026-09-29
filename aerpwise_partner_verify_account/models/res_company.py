from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    partner_verify_account_enabled = fields.Boolean(
        string='Require Verified Partner on Invoices and Bills',
        default=False,
        help=(
            'If enabled, customer invoices and vendor bills cannot be posted '
            'unless the partner (commercial partner) is verified.'
        ),
    )
