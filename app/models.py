from app.database import get_db

class Producto:

    def __init__(self, id_producto=None, nombre=None, fabricante=None, codigo_barra=None, due_date=None, 
                 sale_price=None, cost_price=None, ganancia=None, stock=None,  categoria=None, banner=None):

        self.id_producto=id_producto
        self.nombre=nombre
        self.fabricante=fabricante
        self.codigo_barra=codigo_barra
        self.due_date=due_date
        self.sale_price=sale_price
        self.cost_price=cost_price
        self.ganancia=ganancia
        self.stock=stock
        self.categoria=categoria
        self.banner=banner
 
    def serialize(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'fabricante': self.fabricante,
            'codigo_barra': self.codigo_barra,
            'due_date': self.due_date,   #.strftime('%Y-%m-%d'),
            'sale_price': self.sale_price,
            'cost_price': self.cost_price,
            'ganancia': self.ganancia,
            'stock': self.stock,
            'categoria': self.categoria,
            'banner': self.banner
        }
    

    @staticmethod
    def get_all():

        db = get_db() #recibe de get_db la conexión g.db ----> db=g.db
        cursor = db.cursor()
        query = "SELECT * FROM producto"
        cursor.execute(query)
        rows = cursor.fetchall() #me permite obtener todos los resultados que fueron ejecutados por la query, devuelve una lista de tuplas
        
        producto = [ Producto(id_producto=row[0], nombre=row[1], fabricante=row[2], codigo_barra=row[3], 
                              due_date=row[4], sale_price=row[5], cost_price=row[6], ganancia=row[7], 
                              stock=row[8], categoria=row[9], banner=row[10])
                     for row in rows]
        
        cursor.close()

        return producto



    @staticmethod
    def get_by_id(producto_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM producto WHERE id_producto = %s", (producto_id,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            return Producto(id_producto=row[0], nombre=row[1], fabricante=row[2], codigo_barra=row[3], 
                            due_date=row[4], sale_price=row[5], cost_price=row[6], ganancia=row[7], 
                            stock=row[8], categoria=row[9], banner=row[10])
        return None
       



    """
    Insertar un registro si no existe el atributo id_producto
    """
    def save(self):
        db = get_db()
        cursor = db.cursor()
        self.sale_price = float(self.sale_price)
        self.cost_price = float(self.cost_price)
        self.ganancia = self.sale_price - self.cost_price
        if self.id_producto:
            cursor.execute("""
                UPDATE producto SET nombre = %s, fabricante = %s, codigo_barra = %s, due_date = %s, sale_price = %s,
                            cost_price = %s, ganancia = %s, stock = %s, categoria = %s, banner = %s
                WHERE id_producto = %s
            """, (self.nombre, self.fabricante, self.codigo_barra, self.due_date, self.sale_price, self.cost_price, 
                  self.ganancia, self.stock, self.categoria, self.banner, self.id_producto))
        else:
            cursor.execute("""
                INSERT INTO producto (nombre, fabricante, codigo_barra, due_date, sale_price,
                            cost_price, ganancia, stock, categoria, banner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (self.nombre, self.fabricante, self.codigo_barra, self.due_date, self.sale_price, self.cost_price, 
                  self.ganancia, self.stock, self.categoria, self.banner))
            self.id_producto = cursor.lastrowid
        db.commit()
        cursor.close()


    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM producto WHERE id_producto = %s", (self.id_producto,))
        db.commit()
        cursor.close()
