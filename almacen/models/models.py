# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class almacen(models.Model):
#     _name = 'almacen.almacen'
#     _description = 'almacen.almacen'

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

class mozos(models.Model):
    _name = 'almacen.mozos'
    _description = 'Define los atributos de los mozos'

    #Atributos
    dniMozo = fields.Char(string='Dni', required=True)
    nombreMozo = fields.Char(string='Nombre y Apellidos', required=True)
    fechaNacimiento = fields.Date(string='Fecha Nacimiento', required=True, default=fields.date.today())
    turnoTrabajo = fields.Selection(string='Turno', selection=[('f', 'Dia'), ('b', 'Tarde'), ('c', 'Noche')], help='Turno de trabajo al que se esta destinado')
    edad = fields.Integer(string='Edad', compute='_getEdad')


    #Relacion de tablas
    edad = fields.Integer('Edad', compute='_getEdad')
    productos_id = fields.One2many('almacen.productos','mozos_id', string='Productos')




    def name_get(self):
        mozosDeAlmacen = []
        for mozos in self:
            mozosDeAlmacen.append((mozos.id, mozos.nombreMozo))
        return mozosDeAlmacen


    @api.depends('fechaNacimiento')
    def _getEdad(self):
        hoy = date.today()
        for mozos in self:
            mozos.edad = relativedelta(hoy, mozos.fechaNacimiento).years


    @api.constrains('fechaNacimiento')
    def _checkEdad(self):
        for mozos in self:
            if (mozos.edad < 18):
                raise exceptions.ValidationError("El mozo necesita permiso de sus padres para poder trabajar")


    @api.constrains('dniMozo')
    def _checkDni(self):
        for mozos in self:
            if (len(mozos.dniMozo) > 9):
                raise exceptions.ValidationError("El DNI no puede tener mas de 9 digitos")
            if (len(mozos.dniMozo) < 9):
                raise exceptions.ValidationError("El DNI no puede tener menos de 9 digitos")





class productos(models.Model):
    _name = 'almacen.productos'
    _description = 'Define los atributos de los productos'


    #Atributos
    idProducto = fields.Integer(string='id', required=True)
    nombreProducto = fields.Char(string='Nombre Producto', required=True)
    fechaEntrada = fields.Date(string='Fecha Entrada', required=True, default=fields.date.today())
    fechaSalida = fields.Date(string='Fecha Salida', required=True, default=fields.date.today())
    stock = fields.Integer(string='Stock')


    #Relacion entre tablas
    mozos_id = fields.Many2one('almacen.mozos',  string='Mozos')
    productos_id = fields.Many2one('almacen.productos', string='Productos')


    def name_get(self):
        resultados = []
        for productos in self:
            resultados.append((productos.id, productos.nombreProducto))
        return resultados