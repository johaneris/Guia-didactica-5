"""
Problema#2
Se requiere automatizar un mapa que contiene las estaciones de una ruta previamente
establecida para una aplicación que indique, a partir de un punto de la ruta, el tiempo estimado
para llegar a un destino determinado de la misma.

Contenido de los nodos:
- Estaciones
- Tiempo para la siguiente estación
"""
from linked_list import Ruta

def main():
    new_route: Ruta = Ruta()
    new_route.append("A", 2)
    new_route.append("B", 1)
    new_route.append("C", 4)
    new_route.append("D", 6)
    new_route.append("E", 2)
    
    
    new_route.print_stations()
    
    new_route.expected_time("B","D")
    
if __name__ == "__main__":
    main()