# -*- coding: utf-8 -*-

from odoo import models, fields


class Cliente(models.Model):
    _name = 'gatos.cliente'
    _description = 'Cliente'

    # Campos básicos
    nombre = fields.Char(string='Nombre', required=True)
    edad = fields.Integer(string='Edad')
    telefono = fields.Char(string='Teléfono')
    correo = fields.Char(string='Correo Electrónico')
    foto = fields.Binary("fotoD")
    signo_zodiacal = fields.Selection([
        ('aries', 'Aries'),
        ('tauro', 'Tauro'),
        ('geminis', 'Géminis'),
        ('cancer', 'Cáncer'),
        ('leo', 'Leo'),
        ('virgo', 'Virgo'),
        ('libra', 'Libra'),
        ('escorpio', 'Escorpio'),
        ('sagitario', 'Sagitario'),
        ('capricornio', 'Capricornio'),
        ('acuario', 'Acuario'),
        ('piscis', 'Piscis'),
        ('no_decirlo', 'Prefiero no decirlo'),
    ], string='Signo Zodiacal')
