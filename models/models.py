# -*- coding: utf-8 -*-

from odoo import models, fields, api

class editorial_tematica(models.Model):
    _name = 'editorial.tematica'

    name = fields.Char(string="Nombre de la temática", required=True, help="Introduzca el nombre de la temática")
    descripcion = fields.Text(string="Descripción", help="Introduzca la descripción")

class editorial_revista(models.Model):
    _name = "editorial.revista"

    name = fields.Char(string="Nombre", required=True, help="Introduzca el nombre")
    codigo = fields.Char(string="Código", required=True, help="Introduzca el código")
    numeropaginas = fields.Integer(string="Número de páginas", required=True, help="Introduzca el número de páginas")
    precio = fields.Float(string="Precio", required=True, help="Introduzca el precio")
    rangoprecio = fields.Char(string="Rango de precio", compute="_rangoprecio", store=True)
    tematica = fields.Many2one("editorial.tematica", string="Temática de la revista", required=True, ondelete="cascade")

    @api.depends('precio')
    def _rangoprecio(self):
        for record in self:
            if record.precio >=5:
                record.rangoprecio = "Normal"
            else:
                record.rangoprecio = "Económica"

