from odoo import models,fields

class Client(models.Model):
    _name="freelancer.client"
    _description = 'Client Profile'

    name=fields.Char("Full Name",required=True)
    _is_client = fields.Boolean(default=False)
    company_name=fields.Char(string="Company Name")
    total_spent = fields.Monetary(string="Total Spent", currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string="Currency")

    