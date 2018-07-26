# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = "openclass.course"

    name = fields.Char(string="Tiêu đề", required=True)
    description = fields.Text(string="Mô tả chi tiết")
    name_test = fields.Char()
    date_test = fields.Date(string="Date")

    responsible_id = fields.Many2one('res.users',
                                    ondelete='set null',
                                    string='Responsible',
                                    index=True)
    session_ids = fields.One2many('openclass.session',
                                 'course_id',
                                 string='Session',
                                 required=True)

class Session(models.Model):
    _name = "openclass.session"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2), help="Duration in day")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string='Instructor')
    course_id = fields.Many2one('openclass.course',
                                ondelete='cascade',
                                string='Course',
                                required=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')