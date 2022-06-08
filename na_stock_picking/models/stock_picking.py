from odoo import fields, models, api
from datetime import date, timedelta
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    ddt_supplier_number = fields.Char(string='DDT number', copy=False)
    ddt_supplier_date = fields.Date(string="Delivery date", copy=False)
