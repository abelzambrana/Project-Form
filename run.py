from flask import Flask
from flask_cors import CORS

#Inicialización del proyecto flask
app = Flask(__name__)

CORS(app)





@app.route('/')
def index():
    return '<h1>Hola mundo con flask</h1>'

if __name__=='__main__':
    app.run(debug=True)
           