from flask import Flask
from flask_cors import CORS
from app.views import *
from app.database import init_app

#Inicialización del proyecto flask
app = Flask(__name__)

init_app(app)

CORS(app)

app.route('/api/producto/',methods=['GET'])(get_all_producto)
app.route('/api/producto/<int:producto_id>', methods=['GET'])(get_producto)
app.route('/api/producto/',methods=['POST'])(create_producto)
app.route('/api/producto/<int:producto_id>', methods=['PUT'])(update_producto)
app.route('/api/producto/<int:producto_id>', methods=['DELETE'])(delete_producto)

if __name__=='__main__':
    app.run(debug=True)
           