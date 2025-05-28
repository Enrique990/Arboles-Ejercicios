# Clase que representa una etiqueta HTML como un nodo en un árbol
class NodoHTML:
    def __init__(self, etiqueta, atributos=None):
        self.etiqueta = etiqueta                         # Nombre de la etiqueta (por ejemplo, "div", "p", "span")
        self.atributos = atributos if atributos else {}  # Diccionario de atributos como class, id, etc.
        self.hijos = []                                   # Lista de nodos hijos (etiquetas dentro de esta etiqueta)

    # Método para agregar una etiqueta hija al nodo actual
    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

    # Método para buscar todas las etiquetas con un nombre específico dentro del árbol
    def buscar_etiquetas(self, nombre_etiqueta):
        encontrados = []  # Lista de coincidencias encontradas
        if self.etiqueta == nombre_etiqueta:
            encontrados.append(self)  # Si coincide con el nombre buscado, se agrega
        for hijo in self.hijos:
            encontrados.extend(hijo.buscar_etiquetas(nombre_etiqueta))  # Búsqueda recursiva en los hijos
        return encontrados

    # Método para mostrar la estructura completa del árbol con formato HTML
    def mostrar_estructura(self, nivel=0):
        indent = "  " * nivel  # Espacios para indentación según el nivel del árbol
        atributos = " ".join(f'{k}="{v}"' for k, v in self.atributos.items())  # Formato de los atributos
        print(f"{indent}<{self.etiqueta} {atributos}>")  # Apertura de etiqueta
        for hijo in self.hijos:
            hijo.mostrar_estructura(nivel + 1)  # Llamada recursiva para los hijos
        print(f"{indent}</{self.etiqueta}>")  # Cierre de etiqueta

# Crear la estructura básica del documento HTML (árbol DOM)

# Etiqueta raíz <html>
html = NodoHTML("html")

# Secciones principales
head = NodoHTML("head")
title = NodoHTML("title")
body = NodoHTML("body")

# Añadir head y body como hijos de html
html.agregar_hijo(head)
html.agregar_hijo(body)

# Añadir title dentro de head
head.agregar_hijo(title)

# Crear elementos dentro del body
div = NodoHTML("div", {"class": "container"})     # <div class="container">
p1 = NodoHTML("p")                                # <p>
p2 = NodoHTML("p", {"id": "intro"})               # <p id="intro">
span = NodoHTML("span", {"style": "color:red"})   # <span style="color:red">

# Añadir p1 y span dentro del div
div.agregar_hijo(p1)
div.agregar_hijo(span)

# Añadir div y p2 al body
body.agregar_hijo(div)
body.agregar_hijo(p2)

def mostrar_menu():
    print("\n--- MENÚ DEL DOCUMENTO HTML ---")
    print("1. Mostrar estructura HTML")
    print("2. Buscar etiquetas por nombre")
    print("3. Salir")

# Bucle principal para interactuar con el árbol
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n--- ESTRUCTURA HTML ---\n")
        html.mostrar_estructura()  # Mostrar el documento completo en formato árbol

    elif opcion == "2":
        etiqueta = input("Ingrese el nombre de la etiqueta a buscar: ")
        resultados = html.buscar_etiquetas(etiqueta)  # Buscar etiquetas que coincidan

        if resultados:
            print(f"\nSe encontraron {len(resultados)} etiqueta(s) <{etiqueta}>:")
            for i, nodo in enumerate(resultados, 1):
                print(f"\nEtiqueta #{i}:")
                nodo.mostrar_estructura()  # Mostrar cada coincidencia encontrada
        else:
            print(f"\nNo se encontraron etiquetas <{etiqueta}>.")

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
