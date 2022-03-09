from odoo import fields, models, api
from datetime import date, timedelta
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    ddt_supplier_number = fields.Char(string='Numero DDT')
    ddt_supplier_date = fields.Date(string="Data consegna")
