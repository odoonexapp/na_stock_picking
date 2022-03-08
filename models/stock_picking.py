from odoo import fields, models, api
from datetime import date, timedelta
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    ddt_num = fields.Char(string='Numero DDT')
    delivery_date = fields.Date(string="Data consegna")
    picking_type_value = fields.Char(compute="check_picking_type", stored=1)

    # TODO picking type(done), depends(done) e verifica esistenza record(done)

    @api.depends('picking_type_value')
    def check_picking_type(self):
        stock = self.env['stock.picking'].browse(self.id)
        if stock.id > 0:
            for record in self:
                if stock.picking_type_code == 'incoming':
                    record.picking_type_value = 'incoming'
                elif stock.picking_type_code == 'outgoing':
                    record.picking_type_value = 'outgoing'
        else:
            raise UserError('L\'ordine non esiste.')
