from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_verify_state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('pending', 'To Verify'),
            ('verified', 'Verified'),
            ('rejected', 'Rejected'),
        ],
        string='Verification Status',
        default='draft',
        tracking=True,
        copy=False,
        index=True,
    )
    partner_verify_user_id = fields.Many2one(
        comodel_name='res.users',
        string='Verified By',
        readonly=True,
        copy=False,
        tracking=True,
    )
    partner_verify_date = fields.Datetime(
        string='Verified On',
        readonly=True,
        copy=False,
    )
    partner_verify_note = fields.Text(
        string='Verification Notes',
        copy=False,
        tracking=True,
    )
    partner_is_verified = fields.Boolean(
        string='Is Verified',
        compute='_compute_partner_is_verified',
        search='_search_partner_is_verified',
    )

    @api.depends('partner_verify_state')
    def _compute_partner_is_verified(self):
        for partner in self:
            partner.partner_is_verified = partner.partner_verify_state == 'verified'

    def _search_partner_is_verified(self, operator, value):
        if operator not in ('=', '!='):
            raise UserError(_('Unsupported search operator on verification status.'))

        is_verified = bool(value)
        if operator == '!=':
            is_verified = not is_verified

        if is_verified:
            return [('partner_verify_state', '=', 'verified')]
        return [('partner_verify_state', '!=', 'verified')]

    def _get_partner_to_verify(self):
        self.ensure_one()
        return self.commercial_partner_id or self

    def _get_partner_verify_status_label(self):
        self.ensure_one()
        return self._fields['partner_verify_state'].convert_to_export(
            self.partner_verify_state, self
        )

    def _raise_if_unverified(self, error_msg):
        """Raise if the commercial partner is not verified.

        :param error_msg: format string with %(partner)s and %(status)s
        """
        for partner in self:
            target = partner._get_partner_to_verify()
            if target.partner_verify_state == 'verified':
                continue
            raise UserError(error_msg % {
                'partner': target.display_name,
                'status': target._get_partner_verify_status_label(),
            })

    def action_submit_verify(self):
        for partner in self:
            target = partner._get_partner_to_verify()
            if target.partner_verify_state not in ('draft', 'rejected'):
                raise UserError(_(
                    '%s can only be submitted from Draft or Rejected.'
                ) % target.display_name)
            target.write({
                'partner_verify_state': 'pending',
                'partner_verify_user_id': False,
                'partner_verify_date': False,
            })
            target.message_post(body=_('Submitted for partner verification.'))
        return True

    def action_verify_partner(self):
        if not self.env.user.has_group(
            'aerpwise_partner_verify.group_partner_verify_manager'
        ):
            raise UserError(_('Only Partner Verify Managers can verify contacts.'))

        for partner in self:
            target = partner._get_partner_to_verify()
            if target.partner_verify_state != 'pending':
                raise UserError(_(
                    '%s must be in To Verify before it can be verified.'
                ) % target.display_name)
            target.write({
                'partner_verify_state': 'verified',
                'partner_verify_user_id': self.env.uid,
                'partner_verify_date': fields.Datetime.now(),
            })
            target.message_post(body=_('Partner has been verified.'))
        return True

    def action_reject_verify(self):
        if not self.env.user.has_group(
            'aerpwise_partner_verify.group_partner_verify_manager'
        ):
            raise UserError(_('Only Partner Verify Managers can reject contacts.'))

        partners = self.mapped(lambda p: p._get_partner_to_verify())
        pending = partners.filtered(lambda p: p.partner_verify_state == 'pending')
        if not pending:
            raise UserError(_('Only contacts in To Verify can be rejected.'))

        return {
            'type': 'ir.actions.act_window',
            'name': _('Reject Partner Verification'),
            'res_model': 'partner.verify.reject.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_partner_ids': [(6, 0, pending.ids)],
            },
        }

    def action_reset_verify(self):
        if not self.env.user.has_group(
            'aerpwise_partner_verify.group_partner_verify_manager'
        ):
            raise UserError(_(
                'Only Partner Verify Managers can reset verification.'
            ))

        for partner in self:
            target = partner._get_partner_to_verify()
            if target.partner_verify_state == 'draft':
                continue
            target.write({
                'partner_verify_state': 'draft',
                'partner_verify_user_id': False,
                'partner_verify_date': False,
            })
            target.message_post(body=_('Partner verification has been reset to Draft.'))
        return True
