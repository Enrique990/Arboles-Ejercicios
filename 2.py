import os

class ElementoFS:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Archivo(ElementoFS):
    def __init__(self, nombre, contenido=""):
        super().__init__(nombre)
        self.contenido = contenido
        self.es_directorio = False
    def __str__(self):
        return f"Archivo: {self.nombre}"

class Directorio(ElementoFS):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.hijos = []
        self.es_directorio = True

    def agregar_elemento(self, elemento):
        self.hijos.append(elemento)

    def __str__(self):
        return f"Directorio: {self.nombre}"

def encontrar_ruta_archivo(directorio_raiz, nombre_archivo_buscado):
    
    def buscar_recursivo(directorio_actual, nombre_buscado, ruta_parcial):
        ruta_actual_completa = os.path.join(ruta_parcial, directorio_actual.nombre)

        for elemento in directorio_actual.hijos:
            if not elemento.es_directorio and elemento.nombre == nombre_buscado: # Es un Archivo y coincide el nombre
                return os.path.join(ruta_actual_completa, elemento.nombre)
            elif elemento.es_directorio: # Es un Directorio, buscar dentro
                resultado = buscar_recursivo(elemento, nombre_buscado, ruta_actual_completa)
                if resultado:
                    return resultado
        return None

    if directorio_raiz.nombre == "/":
        ruta_inicial = "" 
    else:
        if not directorio_raiz.hijos:
             return None

        for elemento in directorio_raiz.hijos:
            if not elemento.es_directorio and elemento.nombre == nombre_archivo_buscado:
                return os.path.join(directorio_raiz.nombre, elemento.nombre) if directorio_raiz.nombre != "/" else os.path.join("/", elemento.nombre)

            if elemento.es_directorio:
                ruta_base_para_hijo = directorio_raiz.nombre if directorio_raiz.nombre != "/" else "/"
                resultado = buscar_recursivo(elemento, nombre_archivo_buscado, ruta_base_para_hijo)
                if resultado:
                    return resultado
        return None


    path_inicial = "/" if directorio_raiz.nombre == "/" else ""

    def buscar_recursivo_corregido(directorio_actual, nombre_buscado, ruta_acumulada):
        if ruta_acumulada == "/":
            ruta_directorio_actual = f"/{directorio_actual.nombre}"
            if directorio_actual.nombre == "/":
                ruta_directorio_actual = "/"
        else:
            ruta_directorio_actual = os.path.join(ruta_acumulada, directorio_actual.nombre)


        for elemento in directorio_actual.hijos:
            if not elemento.es_directorio and elemento.nombre == nombre_buscado:
                return os.path.join(ruta_directorio_actual, elemento.nombre)
            elif elemento.es_directorio:
                resultado = buscar_recursivo_corregido(elemento, nombre_buscado, ruta_directorio_actual)
                if resultado:
                    return resultado
        return None

    if directorio_raiz.nombre == "/" :
        return buscar_recursivo_corregido(directorio_raiz, nombre_archivo_buscado, "") 
    else:
        ruta_base = "" 
        resultado_final = buscar_recursivo_corregido(directorio_raiz, nombre_archivo_buscado, ruta_base)
        if resultado_final:
            return "/" + resultado_final if not resultado_final.startswith("/") else resultado_final
        return None


if __name__ == "__main__":
    raiz = Directorio("/")

    home = Directorio("home")
    raiz.agregar_elemento(home)

    usuario = Directorio("usuario")
    home.agregar_elemento(usuario)

    documentos = Directorio("documentos")
    descargas = Directorio("descargas")
    fotos = Directorio("fotos")

    usuario.agregar_elemento(documentos)
    usuario.agregar_elemento(descargas)
    usuario.agregar_elemento(fotos)

    informe_txt = Archivo("informe.txt", "Contenido del informe...")
    presentacion_ppt = Archivo("presentacion.ppt")
    documentos.agregar_elemento(informe_txt)
    documentos.agregar_elemento(presentacion_ppt)

    programa_exe = Archivo("programa.exe")
    imagen_zip = Archivo("imagenes.zip")
    descargas.agregar_elemento(programa_exe)
    descargas.agregar_elemento(imagen_zip)

    vacaciones = Directorio("vacaciones")
    foto_perfil_jpg = Archivo("perfil.jpg")
    fotos.agregar_elemento(vacaciones)
    fotos.agregar_elemento(foto_perfil_jpg)

    playa_jpg = Archivo("playa.jpg")
    montana_png = Archivo("montana.png")
    vacaciones.agregar_elemento(playa_jpg)
    vacaciones.agregar_elemento(montana_png)

    otro_doc = Archivo("otro_documento.txt")
    usuario.agregar_elemento(otro_doc)

    print("Buscando archivos en el sistema:")
    archivos_a_buscar = [
        "informe.txt",
        "presentacion.ppt",
        "programa.exe",
        "perfil.jpg",
        "playa.jpg",
        "montana.png",
        "otro_documento.txt",
        "archivo_inexistente.dat",
        "imagenes.zip"
    ]

    for nombre_fichero in archivos_a_buscar:
        ruta = encontrar_ruta_archivo(raiz, nombre_fichero)
        if ruta:
            print(f"Ruta de '{nombre_fichero}': {ruta}")
        else:
            print(f"Archivo '{nombre_fichero}' no encontrado.")

    print("\n--- Probando con raíz 'mi_raiz' ---")
    mi_raiz = Directorio("mi_raiz")
    carpeta1 = Directorio("carpeta1")
    archivo1_raiz = Archivo("archivo_en_raiz.doc")
    archivo_carpeta1 = Archivo("doc1.txt")

    mi_raiz.agregar_elemento(archivo1_raiz)
    mi_raiz.agregar_elemento(carpeta1)
    carpeta1.agregar_elemento(archivo_carpeta1)

    ruta_test1 = encontrar_ruta_archivo(mi_raiz, "archivo_en_raiz.doc")
    print(f"Ruta de 'archivo_en_raiz.doc': {ruta_test1}")

    ruta_test2 = encontrar_ruta_archivo(mi_raiz, "doc1.txt")
    print(f"Ruta de 'doc1.txt': {ruta_test2}")