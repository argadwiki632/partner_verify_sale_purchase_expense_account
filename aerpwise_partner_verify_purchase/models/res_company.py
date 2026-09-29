from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    partner_verify_purchase_enabled = fields.Boolean(
        string='Require Verified Vendor on Purchase',
        default=False,
        help=(
            'If enabled, purchase orders cannot be confirmed unless the '
            'vendor (commercial partner) is verified.'
        ),
    )
