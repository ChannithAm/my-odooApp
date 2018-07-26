from odoo import fields, models, api
import datetime
class Booking(models.Model):
    _name = 'taxi.booking'


    picking_up = fields.Char(required=True)
    drop_off = fields.Char(required=True)
    pick_up_time = fields.Datetime(required=True)
    booking_time=fields.Datetime(readonly = True)
    other_requirements = fields.Char()

    taken_seats = fields.Integer(string='Taken Seats', required=True)



    # code = fields.Char(string='Code Booking')
    name = fields.Char(readonly=True, string='Code Booking')
    sequence = fields.Integer()
    month = fields.Integer(default=datetime.datetime.utcnow().month)
    year = fields.Integer(default=datetime.datetime.utcnow().year)
    customer_id = fields.Many2one('taxi.customer', string='Customer', required=True, ondelete='set null')


    # now = datetime.datetime.now()
    # month = now.month
    # year = now.year
    # print(month,year)



    @api.model
    def create(self, vals):
        # now = datetime.datetime.now()
        # month = now.month
        # year = now.year
        sql_query = """
                select max(sequence) + 1
                from taxi_booking
                where month = {} and year = {}
            """.format(vals.get('month'), vals.get('year'))
        self._cr.execute(sql_query)
        result = self._cr.fetchone()
        vals['sequence'] = result and result[0] or 1
        vals['name'] = 'BC' \
                       +str(datetime.datetime.utcnow().month)\
                       +str(datetime.datetime.utcnow().year)\
                       + str('-000')\
                       + str(vals.get('sequence'))
        return super(Booking, self).create(vals)
