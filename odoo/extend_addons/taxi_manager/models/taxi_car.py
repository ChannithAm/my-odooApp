from odoo import fields, models, api

class Car(models.Model):
    _name = 'taxi.car'

    name = fields.Char(string='Car Model', required=True)
    license_plates = fields.Char(required=True)
    seat = fields.Integer(required=True)

    driver = fields.Many2one('taxi.driver', required=True, string='Dirver')

    # to Upper case
    # @api.onchange('name')
    # def _set_upper(self):
    #     if self.name:
    #         self.name = str(self.name).upper()
    #     return

    @api.multi
    def name_get(self):
        vals = []
        for car in self:
            if car.id:
                vals.append((car.id,
                             (("".join((car.name).split())).upper())
                             + '-' + (car.license_plates)))
        return vals