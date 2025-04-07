# models/freelancer.py
from odoo import models, fields

class Freelancer(models.Model):
    _inherit = 'res.partner'

    is_freelancer = fields.Boolean(default=False)
    skills = fields.Text(string="Skills")
    rating = fields.Float(string="Rating")
    completed_projects = fields.Integer(string="Completed Projects", default=0)
