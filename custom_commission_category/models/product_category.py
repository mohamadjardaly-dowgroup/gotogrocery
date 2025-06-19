from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    commission_type = fields.Selection([
        ('percentage', 'Percentage'),
    ], string='Commission Type', default='percentage')
    
    commission_amount = fields.Float(
        string='Commission Amount',
        help="Commission amount or percentage based on commission type"
    )
    
    @api.onchange('commission_type')
    def _onchange_commission_type(self):
        """Reset commission amount when type changes"""
        if self.commission_type:
            self.commission_amount = 0.0
