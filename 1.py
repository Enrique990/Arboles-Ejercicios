class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class NodoEmpleado:
    def __init__(self, empleado):
        self.empleado = empleado
        self.subordinados = []

    def agregar_subordinado(self, subordinado_nodo):
        self.subordinados.append(subordinado_nodo)

    def __str__(self):
        return str(self.empleado)

def obtener_nivel_empleado(ceo_nodo, nombre_empleado):
    if not ceo_nodo:
        return -1

    cola = [(ceo_nodo, 0)]

    while cola:
        nodo_actual, nivel_actual = cola.pop(0)

        if nodo_actual.empleado.nombre == nombre_empleado:
            return nivel_actual

        for subordinado in nodo_actual.subordinados:
            cola.append((subordinado, nivel_actual + 1))

    return -1

if __name__ == "__main__":
    ceo = Empleado("Ana (CEO)")
    vp_ventas = Empleado("Carlos (VP Ventas)")
    vp_tecnologia = Empleado("Beatriz (VP Tecnología)")
    gerente_ventas_norte = Empleado("David (Gerente Ventas Norte)")
    gerente_ventas_sur = Empleado("Elena (Gerente Ventas Sur)")
    desarrollador_sr = Empleado("Fernando (Desarrollador Sr.)")
    desarrollador_jr = Empleado("Gabriela (Desarrollador Jr.)")
    soporte_ti = Empleado("Hugo (Soporte TI)")

    nodo_ceo = NodoEmpleado(ceo)
    nodo_vp_ventas = NodoEmpleado(vp_ventas)
    nodo_vp_tecnologia = NodoEmpleado(vp_tecnologia)
    nodo_gerente_ventas_norte = NodoEmpleado(gerente_ventas_norte)
    nodo_gerente_ventas_sur = NodoEmpleado(gerente_ventas_sur)
    nodo_desarrollador_sr = NodoEmpleado(desarrollador_sr)
    nodo_desarrollador_jr = NodoEmpleado(desarrollador_jr)
    nodo_soporte_ti = NodoEmpleado(soporte_ti)

    nodo_ceo.agregar_subordinado(nodo_vp_ventas)
    nodo_ceo.agregar_subordinado(nodo_vp_tecnologia)

    nodo_vp_ventas.agregar_subordinado(nodo_gerente_ventas_norte)
    nodo_vp_ventas.agregar_subordinado(nodo_gerente_ventas_sur)

    nodo_vp_tecnologia.agregar_subordinado(nodo_desarrollador_sr)
    nodo_vp_tecnologia.agregar_subordinado(nodo_desarrollador_jr)
    nodo_vp_tecnologia.agregar_subordinado(nodo_soporte_ti)

    nodo_desarrollador_sr.agregar_subordinado(NodoEmpleado(Empleado("Isabel (Becaria Dev)")))


    print(f"Jerarquía Organizacional:")
    print(f"CEO: {nodo_ceo.empleado.nombre}")
    for vp in nodo_ceo.subordinados:
        print(f"  L-1: {vp.empleado.nombre}")
        for gerente_o_dev in vp.subordinados:
            print(f"    L-2: {gerente_o_dev.empleado.nombre}")
            for sub_nivel3 in gerente_o_dev.subordinados:
                 print(f"      L-3: {sub_nivel3.empleado.nombre}")
    print("-" * 30)

    empleados_a_buscar = [
        "Ana (CEO)",
        "Beatriz (VP Tecnología)",
        "David (Gerente Ventas Norte)",
        "Gabriela (Desarrollador Jr.)",
        "Hugo (Soporte TI)",
        "Isabel (Becaria Dev)",
        "Pedro (No Existe)"
    ]

    for nombre in empleados_a_buscar:
        nivel = obtener_nivel_empleado(nodo_ceo, nombre)
        if nivel != -1:
            print(f"El empleado '{nombre}' está a {nivel} niveles por debajo del CEO.")
        else:
            print(f"El empleado '{nombre}' no fue encontrado en la jerarquía.")