# Clase que representa una categoría como nodo en un árbol
class NodoCategoria:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la categoría
        self.hijos = []       # Lista de subcategorías (nodos hijos)

    # Método para agregar una subcategoría
    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


# Función para buscar todas las subcategorías de una categoría específica
def buscar_subcategorias(nodo, objetivo, encontrado=False, resultados=None):
    if resultados is None:
        resultados = []  # Inicializa la lista de resultados vacía

    if nodo.nombre == objetivo:
        encontrado = True  # Se encontró la categoría objetivo

    if encontrado:
        # Si ya se encontró la categoría, agregar sus subcategorías al resultado
        for hijo in nodo.hijos:
            resultados.append(hijo.nombre)
            # Buscar recursivamente subcategorías dentro de los hijos
            buscar_subcategorias(hijo, objetivo, True, resultados)
    else:
        # Si aún no se encuentra la categoría, buscar en los hijos
        for hijo in nodo.hijos:
            buscar_subcategorias(hijo, objetivo, False, resultados)

    return resultados  # Devuelve todas las subcategorías encontradas


# Función que crea una jerarquía de categorías como ejemplo
def cargar_categorias_ejemplo():
    """
    Crea el siguiente árbol:
    Electrónicos
    ├── Computadoras
    │   ├── Laptops
    │   │   └── Laptops para Juegos
    │   └── PC de Escritorio
    └── Teléfonos
        └── Smartphones
    """
    # Nodo raíz
    electronica = NodoCategoria("Electrónicos")

    # Subcategorías
    computadoras = NodoCategoria("Computadoras")
    laptops = NodoCategoria("Laptops")
    laptops_juegos = NodoCategoria("Laptops para Juegos")
    pcs = NodoCategoria("PC de Escritorio")

    # Construir relaciones
    computadoras.agregar_hijo(laptops)
    computadoras.agregar_hijo(pcs)
    laptops.agregar_hijo(laptops_juegos)

    # Otra rama: teléfonos
    telefonos = NodoCategoria("Teléfonos")
    smartphones = NodoCategoria("Smartphones")
    telefonos.agregar_hijo(smartphones)

    # Agregar ramas principales al nodo raíz
    electronica.agregar_hijo(computadoras)
    electronica.agregar_hijo(telefonos)

    return electronica  # Devuelve el árbol completo


# Función para mostrar un menú interactivo al usuario
def mostrar_menu(raiz):
    """Interfaz para probar la funcionalidad del árbol."""
    while True:
        print("\n=== Menú de Categorías ===")
        print("1. Buscar subcategorías")
        print("2. Ver árbol completo")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            categoria = input("Ingrese la categoría a buscar: ").strip()
            subcategorias = buscar_subcategorias(raiz, categoria)
            print(f"\nSubcategorías de '{categoria}': {subcategorias or 'No encontradas'}")
        elif opcion == "2":
            print("\nÁrbol de Categorías:")
            imprimir_arbol(raiz)
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")


# Función recursiva para imprimir el árbol con indentación
def imprimir_arbol(nodo, nivel=0):
    print("  " * nivel + "└── " + nodo.nombre)  # Imprime la categoría con indentación
    for hijo in nodo.hijos:
        imprimir_arbol(hijo, nivel + 1)  # Llamada recursiva para cada subcategoría


# Punto de entrada del programa
if __name__ == "__main__":
    raiz = cargar_categorias_ejemplo()  # Carga el árbol de ejemplo
    mostrar_menu(raiz)  # Muestra el menú interactivo
