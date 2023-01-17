# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class informacion (models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo para información'
    _sql_constraints = [('nomeUnico', 'unique(name)', 'Non se pode repetir o título')]
    _order = 'descripcion desc'

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
    literal = fields.Char(store=False)
    foto = fields.Binary(string='Foto')
    adxunto_nome = fields.Char(string="Nome Adxunto:")
    adxunto = fields.Binary(string="Arquivo adxunto:")

    # Os campos Many2one crean un campo na BD
    moeda_id = fields.Many2one('res.currency', domain="[('position','=','after')]")
    # con domain, filtramos os valores mostrados. Pode ser mediante unha constante (vai entre comillas) ou unha variable
    #res.currency es el nombre de la BD
    #Relación para buscar en la tabla res.currency con una función lambda
    moeda_euro_id = fields.Many2one('res.currency',
                                    default=lambda self: self.env['res.currency'].search([('name', '=', "EUR")],
                                                                                         limit=1))
    gasto_en_euros = fields.Monetary("Gasto en Euros", 'moeda_euro_id')
    moeda_en_texto = fields.Char(related="moeda_id.currency_unit_label", string="Moeda en formato texto", store=True)
    creador_da_moeda = fields.Char(related="moeda_id.create_uid.login",string="Usuario creador da moeda", store=True)


    @api.depends('alto_en_cms', 'longo_en_cms', 'ancho_en_cms')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) * float(rexistro.ancho_en_cms)

    @api.depends('peso', 'volume')
    def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = float(rexistro.peso) / float(rexistro.volume)
            else:
                rexistro.densidade = 0

    @api.onchange('alto_en_cms')
    def _avisoAlto(self):
        for rexistro in self:
            if rexistro.alto_en_cms > 7:
                rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cms
            else:
                rexistro.literal = ""

    @api.constrains('peso')  # Ao usar ValidationError temos que importar a libreria ValidationError
    def _constrain_peso(self):  # from odoo.exceptions import ValidationError
        for rexistro in self:
            if rexistro.peso < 1 or rexistro.peso > 6:
                raise ValidationError('Os peso de %s ten que ser entre 1 e 4 ' % rexistro.name)


