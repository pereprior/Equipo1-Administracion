# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cliente(models.Model):
    _name = 'feeljoy.cliente'
    _description = 'Cliente'

    foto_perfil = fields.Binary("Foto de perfil")
    nombre = fields.Char(string="Nombre", required=True, help="Introduce un nombre")
    apellidos = fields.Char(string="Apellidos", required=True, help="Introduce los apellidos")
    description = fields.Text(string="Sobre el cliente", required=False, help="Escribe aquí datos de interés del cliente")
    fecha_nacimiento = fields.Date()
    mail = fields.Char(string="Email", required=True, help="Introduce el correo electrónico")
    