from flask import Flask

app = Flask(__name__)

@app.route ('/api/hola')
def hola():
    return('mensaje: ''Prueba de Api')
           
if __name__ == '__main__':
        app.run(debug=True)