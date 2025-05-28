"""
Tarea (Conceptual): Describe cómo se podría utilizar un árbol para representar 
la expresión matemática (3 + 4) * 2. ¿Cuáles serían los nodos y cómo se relacionarían? 
(No se requiere implementación completa, solo la conceptualización de la estructura del árbol).
"""

# Un árbol para representar la expresión matemática (3 + 4) * 2 podría estructurarse de la siguiente manera:
# - El nodo raíz sería el operador de multiplicación (*).
# - El nodo raíz tendría dos hijos:
#   - El primer hijo sería un nodo que representa la operación de suma (+), con dos hijos:
#     - El primer hijo de este nodo sería un nodo hoja que representa el número 3.
#     - El segundo hijo de este nodo sería un nodo hoja que representa el número 4.
#   - El segundo hijo del nodo raíz sería un nodo hoja que representa el número 2.
# Esta estructura permite evaluar la expresión siguiendo las reglas de precedencia de operadores,
# donde primero se evalúa la suma (3 + 4) y luego se multiplica el resultado por 2.

"""
         (*)
        /   \
      (+)    2
     /   \
    3     4
    # En este árbol, los nodos internos representan operaciones y los nodos hoja representan operandos (números).
"""

""" 
¿Qué es un Árbol de Sintaxis Abstracta (AST)?
Un AST es una estructura jerárquica que representa la estructura gramatical del 
código fuente, pero sin los paréntesis ni detalles innecesarios de la sintaxis. 
Solo conserva lo esencial para evaluar o traducir el código.
"""