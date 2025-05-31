from flask import Flask, request, jsonify
from flask_cors import CORS
from pyknow import *

app = Flask(__name__)
CORS(app)  # Permite que el HTML se comunique con el backend

class Sintoma(Fact): pass

class DiagnosticoEngine(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.resultado = "Sin diagnóstico"

    @Rule(Sintoma(nombre='fiebre'), Sintoma(nombre='tos'))
    def gripe(self):
        self.resultado = "Posible Gripe"

    @Rule(Sintoma(nombre='dolor_cabeza'), Sintoma(nombre='náuseas'))
    def migraña(self):
        self.resultado = "Posible Migraña"

@app.route('/diagnostico', methods=['POST'])
def diagnosticar():
    datos = request.json
    engine = DiagnosticoEngine()
    engine.reset()
    for sintoma in datos.get('sintomas', []):
        engine.declare(Sintoma(nombre=sintoma))
    engine.run()
    return jsonify({"diagnostico": engine.resultado})

if __name__ == '__main__':
    app.run(debug=True)
