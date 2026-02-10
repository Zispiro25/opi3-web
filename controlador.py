from flask import Flask, render_template, request, redirect,url_for,session
import json
import requests
import time
app = Flask(__name__)
with(open("key.txt","r")) as f:
    app.secret_key = f.readline() 
from prender_s import prender_server

@app.route("/")
@app.route("/<modo>")
def index(modo = False):
    
    return render_template('password.html', modo = modo)

@app.route("/verificacion_sesion", methods = ['GET'])
def verificacion_sesion():
    return render_template('password.html')

@app.route("/iniciar_sesion", methods = ['POST'])
def iniciar_sesion():
    nombre = request.form['usuario']
    contra = request.form['contra']
    with(open("usuarios.json","r")) as f:
        datos = json.load(f)
        try:
            contraseña = datos[nombre]
            if contra == str(contraseña): 
                session['username'] = nombre
                return redirect(url_for("menu"),code = 303)

                 
            else:
               return redirect(url_for("index", modo = "True"))

        except KeyError as e:
            return {"error" : 'contraseña/usuario incorrecto'}


    
@app.route("/menu", methods=['GET'])
def menu():
    if(session['username'] == None):
        return redirect(url_for("/"))
    else:
        return render_template('main.html')
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
    while True:
        try:
            response = requests.get("http://192.168.100.13:5000/apagar", timeout=10)
        except requests.exceptions.Timeout:
            continue
        try:
            time.sleep(60)
            response = requests.get("http://192.168.100.13:5000/status", timeout=5)
            respuesta = response.json()
        except requests.exceptions.Timeout:
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
