from odoo import fields, models, api
import datetime

class Coordination(models.Model):
    _name = 'taxi.coordination'

    car_model = fields.Many2one('taxi.car', string='Car Model', required=True)
    driver = fields.Many2one('taxi.driver', string='Driver', required=True)
    start_time = fields.Datetime(string='Start Time')

    booking_id = fields.Many2many('taxi.booking', string='Customer')
    pick_up = fields.Char(string='Pick Up', required=False)
    drop_off = fields.Char(string='Drop off', required=False)

    total_of_car_seats = fields.Integer(string='Total of Car Seat', readonly=True)


    # Code
    code = fields.Char(readonly=True, string='Code Coordination')
    sequence = fields.Integer()
    month = fields.Integer(default=datetime.datetime.utcnow().month)
    year = fields.Integer(default=datetime.datetime.utcnow().year)
    # Code
    @api.model
    def create(self, vals):
        sql_query = """
                    select max(sequence) + 1
                    from taxi_coordination
                    where month = {} and year = {}
                """.format(vals.get('month'), vals.get('year'))
        self._cr.execute(sql_query)
        result = self._cr.fetchone()
        vals['sequence'] = result and result[0] or 1
        vals['code'] = 'BC' \
                       + str(datetime.datetime.utcnow().month) \
                       + str(datetime.datetime.utcnow().year) \
                       + str('-000') \
                       + str(vals.get('sequence'))
        return super(Coordination, self).create(vals)


    @api.onchange('booking_id')
    def _onchange(self):
        if self.booking_id:
            self.pick_up = self.booking_id.picking_up
            self.drop_off = self.booking_id.drop_off

    @api.onchange('car_model')
    def _onchange(self):
        if self.car_model:
            self.total_of_car_seats = self.car_model.seat