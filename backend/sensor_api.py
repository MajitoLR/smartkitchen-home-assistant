from flask import Flask, request, jsonify

app = Flask(__name__)

datos_sensor = {
    "temperatura": 0
}

@app.route('/temperature', methods=['POST'])
def recibir_temperatura():

    data = request.json

    datos_sensor["temperatura"] = data["temp"]

    return jsonify({
        "mensaje": "Temperatura recibida"
    })

@app.route('/temperature', methods=['GET'])
def obtener_temperatura():

    return jsonify(datos_sensor)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
