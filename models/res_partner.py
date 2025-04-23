from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'  
    _description = 'Freelancer Profile'
    is_client = fields.Boolean(string="Is a Client")
