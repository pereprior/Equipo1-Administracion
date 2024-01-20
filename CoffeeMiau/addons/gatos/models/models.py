# -*- coding: utf-8 -*-

from odoo import models, fields


class Cliente(models.Model):
    _name = 'gatos.cliente'
    _description = 'Cliente'

    # Campos básicos
    name = fields.Char(string='Nombre', required=True)
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
    gatos_favoritos = fields.Many2many('gatos.gato', string='Gatos Favoritos')
    adopcion = fields.One2many('gatos.adopcion', 'cliente', string='Información de adopcion')
    
class Gatos(models.Model):
    _name = 'gatos.gato'
    _description = 'Gatos'

    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre del gato")
    foto = fields.Binary(string="Foto")
    edad = fields.Integer(string="Edad del gato")
    raza = fields.Char(string="Raza", help="Introduce la raza del gato")
    protectora = fields.Char(string="Protectora", help="Introduce la protectora que se hace cargo del gato")
    personalidad = fields.Char(string="Personalidad", help="Introduce la personalidad del gato")
    info_medica = fields.One2many('gatos.info_medica', 'gato', string='Información Medica')
    adopcion = fields.One2many('gatos.adopcion', 'gato', string='Información de adopcion')

    cliente_id = fields.Many2one('gatos.cliente', string='Cliente')

class Info_Medica(models.Model):
    _name = 'gatos.info_medica'
    _description = 'Informacion medica'

    name = fields.Char(string="Nombre del tutor")
    gato = fields.Many2one('gatos.gato')
    peso = fields.Float(string="Peso", required=True)
    castrado = fields.Boolean(string="Esta castrado", required=True)
    enfermedad = fields.Text(string="Enfermedades u operaciones", required=True, help="Introduce algun tipo de enfermedad u operacion que haya pasado")
    otros = fields.Text(string="Informacion adicional", required=True, help="Introduce informacion adicional relevante")

class Adopcion(models.Model):
    _name = 'gatos.adopcion'
    _description = 'Adopción'

    gato = fields.Many2one('gatos.gato', string='Gato', required=True)
    cliente = fields.Many2one('gatos.cliente', string='Cliente', required=True)
    tipo_vivienda = fields.Selection([
    ('casa', 'Casa'),
    ('piso', 'Piso'),
    ('apartamento', 'Apartamento'),
    ('chalet', 'Chalet'),
    ('duplex', 'Dúplex'),
    ('atico', 'Ático'),
    ('casa_rural', 'Casa Rural'),
    ('otro', 'Otro'),
    ], string='Tipo de Vivienda', required=True)
    mascotas_previas = fields.Selection([
        ('si_gatos', 'Sí, Gatos'),
        ('si_perros', 'Sí, Perros'),
        ('si_otros', 'Sí, Otros'),
        ('si_perros_gatos_otros', 'Sí, Perros, Gatos y/u Otros'),
        ('no', 'No'),
    ], string='¿Has tenido mascotas previas?', required=True)