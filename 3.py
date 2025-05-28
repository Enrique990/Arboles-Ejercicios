class NodoDecision: # Clase para representar un nodo en el árbol de decisiones
    def __init__(self, pregunta=None, diagnostico=None): # Inicializa un nodo con una pregunta o diagnóstico
        self.pregunta = pregunta # Pregunta que se hace al usuario
        self.diagnostico = diagnostico # Diagnóstico final si es un nodo hoja
        self.si = None  # Rama para respuesta "sí"
        self.no = None  # Rama para respuesta "no"

# Nodos hoja (diagnósticos)
diagnostico1 = NodoDecision(diagnostico="El dispositivo funciona correctamente.")
diagnostico2 = NodoDecision(diagnostico="Problema con la pantalla.")
diagnostico3 = NodoDecision(diagnostico="Falla interna del sistema.")
diagnostico4 = NodoDecision(diagnostico="Cargar el dispositivo.")

# Nodos intermedios (preguntas)
pregunta2 = NodoDecision(pregunta="¿Funciona la pantalla?")
pregunta2.si = diagnostico1
pregunta2.no = diagnostico2

pregunta3 = NodoDecision(pregunta="¿Está cargado?")
pregunta3.si = diagnostico3
pregunta3.no = diagnostico4

# Nodo raíz
raiz = NodoDecision(pregunta="¿El dispositivo enciende?")
raiz.si = pregunta2
raiz.no = pregunta3

# Función para recorrer el árbol de decisiones
def diagnosticar(nodo):
    while nodo:
        if nodo.diagnostico:
            print("\nDiagnóstico:", nodo.diagnostico)
            return
        respuesta = input(nodo.pregunta + " (si/no): ").strip().lower()
        if respuesta in ["sí", "si", "s"]:
            nodo = nodo.si
        elif respuesta == "no" or respuesta == "n":
            nodo = nodo.no
        else:
            print("Por favor responde 'sí' o 'no'.")

# Ejecutar el diagnóstico
if __name__ == "__main__":
    print("🛠️ Asistente de diagnóstico para dispositivo electrónico 🛠️\n")
    diagnosticar(raiz)

