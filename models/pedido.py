
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class pedido(models.Model):
    _name = 'odoo_basico.pedido'
    _description = 'Exemplo para pedido'

    name = fields.Char(required=True, size=20, string="Identificador de pedido")
    # Os campos One2many Non se almacenan na BD
    lineapedido_ids = fields.One2many("odoo_basico.linea_pedido", 'pedido_id')