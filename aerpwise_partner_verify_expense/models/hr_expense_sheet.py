from odoo import models, _


class HrExpenseSheet(models.Model):
    _inherit = 'hr.expense.sheet'

    def _get_partners_to_verify(self):
        self.ensure_one()
        partners = self.env['res.partner']
        work_contact = self.employee_id.sudo().work_contact_id
        if work_contact:
            partners |= work_contact
        partners |= self.expense_line_ids.mapped('vendor_id')
        return partners

    def _check_partner_verify(self):
        for sheet in self:
            if not sheet.company_id.partner_verify_expense_enabled:
                continue
            sheet._get_partners_to_verify()._raise_if_unverified(_(
                'Expense report cannot continue because %(partner)s is not '
                'verified (status: %(status)s).'
            ))

    def _do_submit(self):
        self._check_partner_verify()
        return super()._do_submit()

    def _do_approve(self):
        self._check_partner_verify()
        return super()._do_approve()
