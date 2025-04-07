from odoo import models,fields,api

class Project(models.Model):
 _name = 'freelance.project'
_inherit = ['mail.thread', 'mail.activity.mixin']
_description = 'Freelance Project'
name=fields.Char(required=True)
_description=fields.Text()
client_id=fields.Many2one('res.partner',domain="[('is_client','=',True)]",string="Client",required=True)
budget = fields.Monetary()
currency_id = fields.Many2one('res.currency', string="Currency", required=True)
deadline = fields.Date()
state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open for Bids'),
        ('in_progress', 'In Progress'),
        ('done', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='draft', tracking=True)
bid_ids = fields.One2many('freelance.bid', 'project_id', string="Bids")
contract_id = fields.Many2one('freelance.contract', string="Contract")





  