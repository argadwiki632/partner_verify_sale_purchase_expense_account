from odoo import fields, models, _
from odoo.exceptions import UserError


class PartnerVerifyRejectWizard(models.TransientModel):
    _name = 'partner.verify.reject.wizard'
    _description = 'Reject Partner Verification'

    partner_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Partners',
        required=True,
    )
    note = fields.Text(
        string='Rejection Reason',
        required=True,
    )

    def action_reject(self):
        self.ensure_one()
        if not self.env.user.has_group(
            'aerpwise_partner_verify.group_partner_verify_manager'
        ):
            raise UserError(_('Only Partner Verify Managers can reject contacts.'))

        for partner in self.partner_ids:
            if partner.partner_verify_state != 'pending':
                raise UserError(_(
                    '%s must be in To Verify before it can be rejected.'
                ) % partner.display_name)
            partner.write({
                'partner_verify_state': 'rejected',
                'partner_verify_user_id': False,
                'partner_verify_date': False,
                'partner_verify_note': self.note,
            })
            partner.message_post(body=_(
                'Partner verification rejected: %s'
            ) % self.note)
        return {'type': 'ir.actions.act_window_close'}
