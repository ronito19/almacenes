# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class envios(models.Model):
#     _name = 'envios.envios'
#     _description = 'envios.envios'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, exceptions, api

class transportistas(models.Model):
    _name = 'envios.transportistas'
    _description = 'Define los atributos de los transportistas'

    #Atributos
    dniTransportista = fields.Char(string='Dni', required=True)
    nombreTransportista = fields.Char(string='Nombre y Apellidos', required=True)
    numeroPedido = fields.Char(string='Numero Pedido')
    nombreProducto = fields.Char(string='Nombre Producto')
    fechaReparto = fields.Date(string='Fecha Reparto', default=fields.date.today())
    cantidadProducto = fields.Integer(string='Cantidad', compute='_checkCantidad')
    kilosCarga = fields.Integer(string='Kilos', compute='_checkKilos')


    #Relacion de tablas
    vehiculos_id = fields.One2many('envios.vehiculos','transportistas_id', string='Vehiculos')

    def name_get(self):
        transportistasDeCarga = []
        for transportistas in self:
            transportistasDeCarga.append((transportistas.id, transportistas.nombreTransportista))
        return transportistasDeCarga


    @api.constrains('cantidadProducto')
    def _checkCantidad(self):
        for transportistas in self:
            if (len(transportistas.cantidadProducto) > 50):
                raise exceptions.ValidationError("El VEHICULO tiene que ser un camion")
            if (len(transportistas.cantidadProducto) < 50):
                raise exceptions.ValidationError("El VEHICULO tiene que ser una furgoneta")


    @api.constrains('kilosCarga')
    def _checkKilos(self):
        for transportistas in self:
            if (len(transportistas.kilosCarga) > 50):
                raise exceptions.ValidationError("Los PRODUCTOS son pesados")
            if (len(transportistas.kilosCarga) < 50):
                raise exceptions.ValidationError("Los PRODUCTOS no son pesados")



class vehiculos(models.Model):
    _name = 'envios.vehiculos'
    _description = 'Define los atributos de los vehiculos'


    #Atributos
    idVehiculo = fields.Integer(string='id', required=True)
    matriculaVehiculo = fields.Char(string='Matricula', required=True)
    marcaVehiculo = fields.Char(string='Marca', required=True)
    tamañoVehiculo = fields.Selection(string='Tamaño', selection=[('f', 'Furgoneta'), ('b', 'Camion')], help='Tamaño del vehiculo para los productos')
    nombreTransportista = fields.Char(string='Nombre y Apellidos', required=True)


    #Relacion entre tablas
    transportistas_id = fields.Many2one('envios.transportistas', string='Transportistas')
    vehiculos_id = fields.Many2one('envios.vehiculos', string='Vehiculos')


    def name_get(self):
        resultados = []
        for vehiculos in self:
            resultados.append((vehiculos.id, vehiculos.matriculaVehiculo))
        return resultados