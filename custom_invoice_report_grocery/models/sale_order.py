from odoo import models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)
        res.update({
            'product_packaging_id': self.product_packaging_id.id,
            'product_packaging_qty': self.product_packaging_qty,
        })
        return res
