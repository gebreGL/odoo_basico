# -*- coding: utf-8 -*-

from odoo import models, fields, api


class linea_pedido(models.Model):
    _name = 'odoo_basico.linea_pedido'
    _description = 'Exemplo para linea_pedido'

    name = fields.Char(required=True, size=20, string="Nome da linea pedido")
    descripcion_linea_pedido = fields.Text(string="A Descripción da linea pedido")  # string é a etiqueta do campo
    # Relación con el módulo 'pedido.py'
      #Para usar una One2Many hace falta crear una Many2One
    pedido_id = fields.Many2one('odoo_basico.pedido',ondelete="cascade", required=True)

