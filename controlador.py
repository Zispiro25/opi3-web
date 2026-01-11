from flask import Flask, render_template, request
import requests
app = Flask(__name__)
from prender_s import prender_server
@app.route("/")
def index():
    return render_template('password.html')

@app.route("/verificacion_sesion", methods = ['GET'])
def verificacion_sesion():
    return render_template('password.html')

@app.route("/iniciar_sesion", methods = ['POST'])
def iniciar_sesion():
    nombre = request.form['usuario']
    contra = request.form['contra']
    request.cookies.set("username", nombre)
    
    if nombre == "admin" and contra == "123":
        return render_template('main.html')
    else:
        return 'contraseña/usuario incorrecto'
    
@app.route("/prender", methods=['GET'])
def prender():
    estado = "activado"
    prender = prender_server()
    if(prender):
        return {"estado" : estado}
    else:
        estado = "error"
        return {"estado" : estado}
    
@app.route("/apagar_server", methods=['GET'])
def apagar():
    try:
        response = requests.get("http://192.168.100.13:5000/apagar", timeout = 10)
    except requests.exceptions.Timeout:
        return {"estado":"apagado"}
    finally:
       return {"estado" : "apagado"}
    

@app.route("/status_server", methods=['GET'] )
def status():
    try:
        response = requests.get("http://192.168.100.13:5000/status", timeout=5)
        respuesta = response.json()
    except requests.exceptions.Timeout:
        return {"estado":"apagado"}
    if(respuesta["estado"] == "prendido"):
        return {"estado" : "prendido"}
