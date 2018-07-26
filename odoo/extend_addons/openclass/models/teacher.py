from  odoo import models, fields

class Teacher(models.Model):
    _inherit = 'openclass.teacher'

    name = fields.Char(string="Name of Teacher", required=True)