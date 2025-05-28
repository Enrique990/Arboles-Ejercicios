class Persona: # Clase para representar a una persona en el árbol genealógico
    def __init__(self, nombre, padre=None, madre=None): # Inicializa una persona con su nombre y sus padres
        self.nombre = nombre # Nombre de la persona
        self.padre = padre # Padre de la persona (otro objeto Persona)
        self.madre = madre # Madre de la persona (otro objeto Persona)

    def __str__(self): # Método para representar la persona como string
        return self.nombre

# =====================
# Crear el árbol genealógico
# =====================

# Generación 3 (bisabuelos)
abuelo_paterno_p = Persona("Juan")
abuela_paterna_p = Persona("María")
abuelo_materno_p = Persona("Carlos")
abuela_materna_p = Persona("Elena")
abuelo_paterno_m = Persona("Pedro")
abuela_paterna_m = Persona("Laura")
abuelo_materno_m = Persona("Miguel")
abuela_materna_m = Persona("Rosa")

# Generación 2 (abuelos)
padre = Persona("Roberto", abuelo_paterno_p, abuela_paterna_p)
madre = Persona("Lucía", abuelo_materno_p, abuela_materna_p)
padre_madre = Persona("Antonio", abuelo_paterno_m, abuela_paterna_m)
madre_madre = Persona("Carmen", abuelo_materno_m, abuela_materna_m)

# Generación 1 (padres del protagonista)
papá = Persona("José", padre, madre)
mamá = Persona("Ana", padre_madre, madre_madre)

# Generación 0 (protagonista)
yo = Persona("Tú", papá, mamá)

# =====================
# Función para obtener ancestros en una generación específica
# =====================

def obtener_ancestros(persona, generacion):
    if persona is None: # Si la persona es la raíz o no existe, retorna una lista vacía, lo que indica que no hay ancestros
        return []
    if generacion == 0: # Si la generación es 0, retorna la persona actual (tú)
        return [persona]
    ancestros = [] # Lista para almacenar los ancestros encontrados
    ancestros += obtener_ancestros(persona.padre, generacion - 1) # Llama recursivamente a la función para obtener los ancestros del padre
    ancestros += obtener_ancestros(persona.madre, generacion - 1) # Llama recursivamente a la función para obtener los ancestros de la madre
    return ancestros # Retorna la lista de ancestros encontrados en la generación especificada

# =====================
# Ejecutar el programa
# =====================

if __name__ == "__main__":
    print("👪 Árbol Genealógico: Ancestros en Generación Específica\n")
    try:
        gen = int(input("¿Qué generación quieres consultar? (0 = tú, 1 = padres, 2 = abuelos, 3 = bisabuelos): "))
        ancestros = obtener_ancestros(yo, gen)

        if ancestros:
            print(f"\nAncestros en la generación {gen}:") # Muestra los ancestros encontrados en la generación especificada
            for persona in ancestros:
                print("-", persona) # Muestra el nombre de cada ancestro encontrado
        else:
            print("No se encontraron ancestros en esa generación.")
    except ValueError:
        print("Por favor, introduce un número entero válido.")


