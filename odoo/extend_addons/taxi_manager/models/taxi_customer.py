from odoo import fields, models, api

class Taxi(models.Model):
    _name = 'taxi.customer'

    name = fields.Char(required=True)
    mobile_phone = fields.Char(required=True)
    last_pick_up = fields.Char()
    last_drop_off = fields.Char()

    # name_combine = fields.Char(string='Combine Name')

    # Convert to upper case
    # @api.onchange('name')
    # def _set_upper(self):
    #     if self.name:
    #         self.name = str(self.name).upper()
    #     return

    # Combine 'name - mobile phone'
    # @api.one
    # @api.depends('name', 'mobile_phone')
    # def _compute_display_name(self):
    #     names = [self.name, self.mobile_phone]
    #     self.name_combine = ' - '.join(filter(None, names))

    # to Booking
    @api.multi
    def name_get(self):
        vals = []
        for customer in self:
            if customer.id:
                vals.append((customer.id,
                             (("".join((customer.name).split())).upper())
                             + '-' + (customer.mobile_phone)))
        return vals