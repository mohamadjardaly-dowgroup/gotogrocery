from odoo import models, fields,api

class AccountMove(models.Model):
    _inherit = 'account.move'

    representive_name = fields.Char(string="Representative Name")

    total_weight = fields.Float(string="Total Weight", compute="_compute_total_weight", store=True)

    tax_in_other_curr = fields.Monetary(
        string="Tax Curr",
        compute="_compute_tax_in_other_curr",
        currency_field='company_currency_id',
        store=True
    )

    @api.depends("line_ids.tax_line_id")
    def _compute_tax_in_other_curr(self):
        for record in self:
            tax_total = 0.0
            for line in record.line_ids.filtered(lambda l: l.tax_line_id and '%' in l.name):
                tax_total +=  line.credit  # Adjust this logic based on your tax structure
            record.tax_in_other_curr = tax_total


    @api.depends('invoice_line_ids.product_id', 'invoice_line_ids.quantity')
    def _compute_total_weight(self):
        for move in self:
            total_weight = sum(
                line.product_id.weight * line.quantity for line in move.invoice_line_ids if line.product_id.weight)
            move.total_weight = total_weight


    @api.depends('invoice_line_ids.product_id', 'invoice_line_ids.quantity')
    def _compute_total_weight(self):
        for move in self:
            total_weight = sum(
                line.product_id.weight * line.quantity for line in move.invoice_line_ids if line.product_id.weight)
            move.total_weight = total_weight




class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    product_packaging_id = fields.Many2one('product.packaging', string="Product Packaging")
    product_packaging_qty = fields.Float( string="Product Packaging Qty")