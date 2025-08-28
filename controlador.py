from flask import Flask, render_template, request
from prender_s import prender_server, apagar_server
from threading import Thread
from time import time
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
        
        return render_template('main.html')
    else:
        return 'contraseña/usuario incorrecto'
    
@app.route("/main/<orden>", methods=['POST'])
def comando_server(orden):
    if orden == "apagar":
        hilo = Thread(target=apagar_server)
        hilo.start()
        #verificar que despues de cierto tiempo mate el hilo
        i = time()
        while(True):
            f = time()
            if( f - i > 30):
                break
        #terminar cuando se sepa javascript
        

    elif orden == "prender":
        prender_server()
        return render_template("main.html")
        #lo mismo, colocar una alerta o algo