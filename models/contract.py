from odoo import models, fields

class FreelanceContract(models.Model):
    _name = 'freelance.contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Freelance Contract'

    project_id = fields.Many2one('freelance.project', required=True)
    freelancer_id = fields.Many2one('freelancer.freelancer', domain="[('is_freelancer','=',True)]", required=True)
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date()
    agreed_amount = fields.Monetary()
    currency_id = fields.Many2one('res.currency', string="Currency")
    milestone_details = fields.Text()
    invoice_id = fields.Many2one('account.move', string="Invoice")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='draft', tracking=True)
