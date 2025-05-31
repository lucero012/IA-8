from pyknow import *

class Sintoma(Fact):
    """Clase para representar un síntoma"""
    pass

class DiagnosticoMedico(KnowledgeEngine):

    @Rule(Sintoma(nombre='fiebre'))
    @Rule(Sintoma(nombre='tos'))
    def posible_gripe(self):
        print("Posible diagnóstico: Gripe")

    @Rule(Sintoma(nombre='dolor_cabeza'), Sintoma(nombre='náuseas'))
    def posible_migraña(self):
        print("Posible diagnóstico: Migraña")

# Ejecución
engine = DiagnosticoMedico()
engine.reset()
engine.declare(Sintoma(nombre='fiebre'))
engine.declare(Sintoma(nombre='tos'))
engine.run()
