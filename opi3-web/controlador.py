from flask import Flask, render_template, request
from prender_s import prender_server
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/verificacion_sesion", methods = ['GET'])
def verificacion_sesion():
    return render_template('password.html')
@app.route("/iniciar_sesion", methods = ['POST'])
def iniciar_sesion():
    #esto es de prueba, en prod eliminar y usar un json o algo
    nombre = request.form['usuario']
    contra = request.form['contra']
    if nombre == "admin" and contra == "123":
        prender_server()
        return render_template('main.html')
    else:
        return 'contraseña/usuario incorrecto'
    