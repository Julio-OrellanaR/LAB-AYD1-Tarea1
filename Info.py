from locale import atoi
from flask import Flask, jsonify, render_template, request,send_file
from Crypto.Cipher import AES  #Works

app = Flask(__name__, template_folder='plantillas')

@app.route('/op', methods = ["GET"])

def formulario():
    
    return render_template('plantilla.html')

@app.route('/op', methods = ["POST"])

def resta():
    numero1 = request.form['numero1']
    numero2 = request.form['numero2']
    op1 = atoi(numero1) - atoi(numero2)

    resp = {"Resultado de operacion resta es: " : op1}

    return jsonify(resp)

@app.route('/', methods = ["GET"])

def init():
    
    data = "<br /> <b>Nombre:</b> Julio José Orellna Ruíz  <br /><br /> <b> Carnet:</b> 201908120 <br /> <br /> (http://127.0.0.1:3000/op) para ir a restar numeros"

    return data


if __name__ == '__main__':
    app.run(debug=True, port=3000)