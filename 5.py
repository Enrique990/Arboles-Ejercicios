class NodoCDN: # Clase para representar un nodo en el árbol de la CDN
    def __init__(self, region, hijos=None): # Inicializa un nodo con su región y una lista de nodos hijos
        self.region = region  # Ejemplo: "Global", "América", "México", etc.
        self.hijos = hijos or []  # Lista de nodos hijos

    def es_hoja(self): # Método para verificar si el nodo es una hoja (sin hijos)
        return not self.hijos

def construir_arbol_cdn():
    """Crea la jerarquía de la CDN."""
    raiz = NodoCDN("Global") # Nodo raíz de la CDN

    # Servidores regionales (continentes)
    # Aquí se crean nodos para cada continente
    america = NodoCDN("América") 
    europa = NodoCDN("Europa") 
    asia = NodoCDN("Asia") 

    # Servidores locales (países)
    # Aquí se crean nodos para cada país en los continentes
    america.hijos = [NodoCDN("México"), NodoCDN("Brasil"), NodoCDN("Canadá")] 
    europa.hijos = [NodoCDN("España"), NodoCDN("Alemania"), NodoCDN("Francia")] 
    asia.hijos = [NodoCDN("Japón"), NodoCDN("India"), NodoCDN("China")] 

    raiz.hijos = [america, europa, asia] # Agrega los continentes como hijos del nodo raíz
    return raiz # Devuelve el nodo raíz de la CDN

def mostrar_menu_paises(raiz):
    """Muestra un menú interactivo para seleccionar un país de los integrados en el árbol."""
    print("\n **Seleccione un país para encontrar el servidor más cercano:**")
    #Este if es para crear un menú interactivo que muestre los continentes y países disponibles
    for i, continente in enumerate(raiz.hijos, 1): 
        print(f"\n[{i}] {continente.region}:") # Muestra el nombre del continente
        for j, pais in enumerate(continente.hijos, 1): 
            print(f"    {j}. {pais.region}") # Muestra el nombre del país

    # Validar entrada del usuario
    while True: # Crea un bucle para solicitar al usuario que elija un continente y un país
        try: # Crea un bloque try para manejar excepciones y validar errores de entrada
            opcion_continente = int(input("\n- Elija un continente (número): ")) - 1
            if 0 <= opcion_continente < len(raiz.hijos): 
                continente = raiz.hijos[opcion_continente] # Obtiene el continente seleccionado
                opcion_pais = int(input(f"-  Elija un país en {continente.region} (número): ")) - 1
                if 0 <= opcion_pais < len(continente.hijos):
                    return continente.hijos[opcion_pais].region # Devuelve el nombre del país seleccionado
                else:
                    print("Error: Número de país inválido.")
            else:
                print("Error: Número de continente inválido.")
        except ValueError:
            print("Error: Ingrese un número válido.")

def servidor_mas_cercano(raiz, pais_usuario): # Encuentra el servidor más cercano al país seleccionado por el usuario.
    for continente in raiz.hijos: # Recorre los continentes en el árbol de la CDN
        for pais in continente.hijos: # Recorre los países en cada continente
            if pais.region == pais_usuario: # Si el país coincide con el seleccionado por el usuario, devuelve la región del continente
                return continente.region
    return None

# --- Ejecución principal ---
if __name__ == "__main__": 
    cdn = construir_arbol_cdn() # Construye el árbol de la CDN
    pais_elegido = mostrar_menu_paises(cdn) # Muestra el menú de países y obtiene la selección del usuario
    servidor = servidor_mas_cercano(cdn, pais_elegido) # Encuentra el servidor más cercano al país seleccionado

    if servidor: # Si se encontró un servidor, muestra el resultado
        print(f"\n**Resultado:** El servidor más cercano a {pais_elegido} está en {servidor}.")
    else:
        print("\nNo se encontró servidor para el país seleccionado.")