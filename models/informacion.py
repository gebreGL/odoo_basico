# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo para información'

    name = fields.Char(string="Título:")
    descripcion = fields.Text(string="Descripción:")
    peso = fields.Float(string="Peso en KGs:", default=4.5, digits=(6,2))
    sexo_traducido = fields.Selection([('Mujer','Muller'), ('Hombre','Home'), ('Otros','Outros')], string="Sexo:")
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
    alto_en_cms = fields.Integer(string="Altura en cms:")
    ancho_en_cms = fields.Integer(string="Anchura en cms:")
    longo_en_cms = fields.Integer(string="Longo en cms:")
    volume = fields.Float(compute="_volume", store=True)
    densidade = fields.Float(compute="_densidade", store=True)

    @api.depends('alto_en_cms', 'longo_en_cms', 'ancho_en_cms')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) * float(rexistro.ancho_en_cms)

    @api.depends('peso', 'volume')
    def _densidade(self):
        for rexistro in self:
            rexistro.densidade = float(rexistro.peso) / float(rexistro.volume)

