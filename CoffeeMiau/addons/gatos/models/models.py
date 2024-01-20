# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Gatos(models.Model):
    _name = 'gatos.gato'
    _description = 'Gatos'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del gato")
    foto = fields.Binary("foto")
    edad = fields.Integer(string="Edad del gato")
    raza = fields.Char(string="Raza", help="Introduce la raza del gato")
    protectora = fields.Char(string="Protectora", help="Introduce la protectora que se hace cargo del gato")
    personalidad = fields.Char(string="Personalidad", help="Introduce la personalidad del gato")
    info_medica = fields.One2many('gatos.info_medica', 'gato', string='Información Medica')

class Info_Medica(models.Model):
    _name = 'gatos.info_medica'
    _description = 'Informacion medica'

    name = fields.Char(string="Info_Medica")
    gato = fields.Many2one('gatos.gato', string='Gato', required=True)
    peso = fields.Float(string="Peso", required=True)
    castrado = fields.Boolean(string="Esta castrado", required=True)
    enfermedad = fields.Text(string="Enfermedades u operaciones", required=True, help="Introduce algun tipo de enfermedad u operacion que haya pasado")
    otros = fields.Text(string="Informacion adicional", required=True, help="Introduce informacion adicional relevante")