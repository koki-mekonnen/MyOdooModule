# models/bid.py
from odoo import models, fields

class FreelanceBid(models.Model):
    _name = 'freelance.bid'
    _description = 'Freelance Bid'

    project_id = fields.Many2one('freelance.project', required=True)
    freelancer_id = fields.Many2one('freelancer.freelancer', domain="[('is_freelancer','=',True)]", required=True)
    proposed_price = fields.Monetary()
    currency_id = fields.Many2one('res.currency', string="Currency", required=True)
    proposal = fields.Text()
    is_accepted = fields.Boolean(default=False)
