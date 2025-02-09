from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SalesOrderCustomization(models.Model):
    _inherit = 'sale.order'

    discount_amount = fields.Float(
        string=_('Discount Amount'),
    )
    total_amount_after_discount = fields.Float(
        string=_('Total Amount After Discount'),
        compute='_get_total_amount_after_discount',
        store=True,
    )

    @api.depends('amount_total', 'discount_amount')
    def _get_total_amount_after_discount(self):
        for order in self:
            order.total_amount_after_discount = order.amount_total - order.discount_amount
