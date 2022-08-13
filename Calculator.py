#from crypt import methods
from locale import atoi
from unicodedata import name
from flask import Flask, jsonify, render_template, request,send_file
from Crypto.Cipher import AES  #Works

app = Flask(__name__, template_folder='plantillas')

@app.route('/', methods = ["GET"])

def formulario():
    
    return render_template('plantilla.html')

@app.route('/', methods = ["POST"])

def suma():
    numero1 = request.form['numero1']
    numero2 = request.form['numero2']
    op = atoi(numero1) + atoi(numero2)
    op1 = numero1 + numero2

    return 'la suma es = ' + str(op1)


if __name__ == '__main__':
    app.run(debug=True, port=3000)