from odoo import fields, models, api


class Driver(models.Model):
    _name = 'taxi.driver'

    name = fields.Char(string='Name',required=True)
    mobile_phone= fields.Char(required=True)
    id_num = fields.Char(string='Identification Number', required=True)
    perm_addr = fields.Char(string='Permenent Addr', required=True)
    temp_addr = fields.Char(string='Temperary Addr')

    # @api.onchange('name')
    # def _set_upper_driver(self):
    #     if self.name:
    #         self.name = str(self.name).upper()
    #     return

    # to Coordination
    @api.multi
    def name_get(self):
        vals = []
        for customer in self:
            if customer.id:
                vals.append((customer.id,
                             (("".join((customer.name).split())).upper())
                             + '-' + (customer.mobile_phone)))
        return vals