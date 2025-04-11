class RedSemantica:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nombre, atributos=None):
        """Agrega un nodo con atributos opcionales"""
        if atributos is None:
            atributos = {}
        self.nodos[nombre] = {'atributos': atributos, 'arcos': []}

    def agregar_arco(self, origen, destino, relacion):
        """Agrega un arco (relación) entre dos nodos"""
        if origen in self.nodos and destino in self.nodos:
            self.nodos[origen]['arcos'].append({'destino': destino, 'relacion': relacion})
        else:
            print(f"Error: Nodo '{origen}' o '{destino}' no existe.")

    def mostrar_red(self):
        """Muestra la red semántica"""
        for nodo, datos in self.nodos.items():
            print(f"\nNodo: {nodo}")
            print(f"  Atributos: {datos['atributos']}")
            for arco in datos['arcos']:
                print(f"  --> {arco['relacion']} --> {arco['destino']}")


# Crear la red semántica
red = RedSemantica()

# Agregar nodos con atributos
red.agregar_nodo("Perro", {"color": "marrón", "tamaño": "mediano", "raza": "Labrador"})
red.agregar_nodo("Mamífero", {"característica": "vertebrado"})
red.agregar_nodo("Ave", {"característica": "vuela"})

# Agregar relaciones (arcos)
red.agregar_arco("Perro", "Mamífero", "es un tipo de")
red.agregar_arco("Perro", "Ave", "no es un tipo de")

# Mostrar la red
red.mostrar_red()
