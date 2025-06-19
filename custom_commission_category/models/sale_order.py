from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_commission = fields.Monetary(
        string='Total Commission',
        compute='_compute_total_commission',
        store=True,
        currency_field='currency_id'
    )

    @api.depends('order_line.commission_amount')
    def _compute_total_commission(self):
        """Calculate total commission for the sale order"""
        for order in self:
            order.total_commission = sum(order.order_line.mapped('commission_amount'))


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    commission_amount = fields.Monetary(
        string='Commission Amount',
        compute='_compute_commission_amount',
        store=True,
        currency_field='currency_id'
    )

    @api.depends('product_id', 'price_subtotal', 'product_id.categ_id.commission_amount', 
                 'product_id.categ_id.commission_type')
    def _compute_commission_amount(self):
        """Calculate commission amount based on product category"""
        for line in self:
            commission = 0.0
            if line.product_id and line.product_id.categ_id:
                category = line.product_id.categ_id
                if category.commission_amount > 0:
                    if category.commission_type == 'percentage':
                        # Calculate percentage of subtotal
                        commission = (line.price_subtotal * category.commission_amount) / 100

            
            line.commission_amount = commission

    @api.onchange('product_id', 'product_uom_qty')
    def _onchange_product_commission(self):
        """Trigger commission recalculation when product or quantity changes"""
        self._compute_commission_amount()
