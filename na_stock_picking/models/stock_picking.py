from odoo import fields, models, api
from datetime import date, timedelta
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    ddt_num = fields.Char(string='Numero DDT')
    delivery_date = fields.Date(string="Data consegna")
