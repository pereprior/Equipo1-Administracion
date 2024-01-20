# -*- coding: utf-8 -*-

from odoo import models, fields, api


class feeljoyLocal(models.Model):
    _name = 'feeljoy.local'
    _description = 'local'

    name = fields.Char(string='Nombre del Local', required=True)
    imagen = fields.Binary(string='Imagen', required=True)
    precioDia = fields.Char(string='Precio', required=True)
    comentarios = fields.Text(string='Comentarios')
    eventos_ids = fields.One2many('feeljoy.evento', 'local_id', string='Eventos')


class FeeljoyCalidadServicio(models.Model):
    _name = 'feeljoy.calidadservicio'
    _description = 'calidadservicio'

    name = fields.Char(string='Nombre de la Calidad del Servicio')
    porcentaje_aumento = fields.Float(string='Porcentaje de Aumento', required=True)
    comentarios = fields.Text(string='Comentarios')


class FeeljoyEvento(models.Model):
    _name = 'feeljoy.evento'
    _description = 'evento'

    name = fields.Char(string='Presupuesto para...')
    local_id = fields.Many2one('feeljoy.local', string='Local', required=True)
    calidad_servicio_id = fields.Many2one('feeljoy.calidadservicio', string='Calidad de Servicio', required=True)
    fecha = fields.Date(string='Fecha del Evento', required=True)
    tipo_evento = fields.Selection([
        ('boda', 'Boda'),
        ('cumpleanos', 'Cumpleaños'),
        ('comunion', 'Comunión'),
        ('aniversario', 'Aniversario'),
        ('despedida_soltero', 'Despedida de Soltero'),
        ('graduacion', 'Graduación'),
        ('conferencia', 'Conferencia'),
        ('reunion_familiar', 'Reunión Familiar'),
        ('inauguracion', 'Inauguración'),
        ('fiesta_tematica', 'Fiesta Temática'),
    ], string='Tipo de Evento', required=True)
    precio_por_invitado = fields.Float(string='Precio por Invitado', required=True)
    cantidad_invitados = fields.Integer(string='Cantidad de Invitados', required=True)
    total_price = fields.Float(string='Precio Total', compute='_compute_total_price', store=True)


    @api.depends('local_id', 'calidad_servicio_id', 'cantidad_invitados', 'precio_por_invitado')
    def _compute_total_price(self):
        for evento in self:
            lugar_precio = float(evento.local_id.precioDia)
            descuento_por_cantidad = 0.0
            if 5 <= evento.cantidad_invitados <= 10:
                descuento_por_cantidad = 0.0
            elif 11 <= evento.cantidad_invitados <= 20:
                descuento_por_cantidad = 1.0
            elif 21 <= evento.cantidad_invitados <= 30:
                descuento_por_cantidad = 2.0
            elif 31 <= evento.cantidad_invitados <= 40:
                descuento_por_cantidad = 4.0
            elif 41 <= evento.cantidad_invitados <= 999:
                descuento_por_cantidad = 5.0

            porcentaje_aumento = evento.calidad_servicio_id.porcentaje_aumento
            precio_lugar = lugar_precio * (1 + porcentaje_aumento / 100)

            precio_invitado = evento.precio_por_invitado
            precio_con_descuento = precio_invitado - (precio_invitado * (descuento_por_cantidad / 100))

            evento.total_price = precio_lugar + (precio_con_descuento * evento.cantidad_invitados)