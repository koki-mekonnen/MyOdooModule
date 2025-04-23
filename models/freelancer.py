# models/freelancer.py
from odoo import models, fields

class Freelancer(models.Model):
    _name="freelancer.freelancer"
    _description = 'Freelancer Profile'

    name=fields.Char("Full Name",required=True)
    age=fields.Integer(string="Age")
    title=fields.Char("Title",required=True)
    skills = fields.Text(string="Skills")
    rating = fields.Float(string="Rating")
    completed_projects = fields.Integer(string="Completed Projects", default=0)
    is_freelancer = fields.Boolean(default=False)
