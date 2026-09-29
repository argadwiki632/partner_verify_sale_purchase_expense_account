from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    partner_verify_sale_enabled = fields.Boolean(
        string='Require Verified Customer on Sales',
        default=False,
        help=(
            'If enabled, sales orders cannot be confirmed unless the '
            'customer (commercial partner) is verified.'
        ),
    )
