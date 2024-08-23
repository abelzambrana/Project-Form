from flask import jsonify, request
from app.models import Producto

def get_all_producto():
 
    producto = Producto.get_all()
    list_producto = [prod.serialize() for prod in producto ]
    return  jsonify(list_producto)


def create_producto():
    #recepcionando los datos enviados en la petición en formato json y los convierte en un diccionario
    data = request.json
    new_producto = Producto(

        nombre=data['nombre'],
        fabricante=data['fabricante'],
        codigo_barra=data['codigo_barra'],
        due_date=data['due_date'],
        sale_price=data['sale_price'],
        cost_price=data['cost_price'],
        ganancia= (data['sale_price'] - data['cost_price']),
        #ganancia=data['ganancia'],
        stock=data['stock'],
        categoria=data['categoria'],
        banner=data['banner']
     )
    new_producto.save()
    return jsonify({'message':'Producto creado con éxito'}), 201    #se envia un codigo 201 por que es el cod de 
                                                                    # resp a htpp cdo se indica que un registro a sido creado

def update_producto(producto_id):
    producto = Producto.get_by_id(producto_id)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    data = request.json

    producto.nombre = data['nombre']
    producto.fabricante = data['fabricante']
    producto.codigo_barra = data['codigo_barra']
    producto.due_date = data['due_date']
    producto.sale_price = data['sale_price']
    producto.cost_price = data['cost_price']
    producto.ganancia = data['ganancia']
    producto.stock = data['stock']
    producto.categoria = data['categoria']
    producto.banner = data['banner']

    producto.save()

    return jsonify({'message': 'Producto actualizado con éxito'})  


def get_producto(producto_id):
    producto = Producto.get_by_id(producto_id)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    return jsonify(producto.serialize())


def delete_producto(producto_id):
    producto = Producto.get_by_id(producto_id)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    producto.delete()
    return jsonify({'message': 'Producto eliminado exitosamente'})
