from odoo import models, fields


class EmployeesCustomization(models.Model):
    _inherit = 'hr.employee'

    overtime_ability = fields.Boolean(
        string="Overtime Ability",
        default=False
    )

