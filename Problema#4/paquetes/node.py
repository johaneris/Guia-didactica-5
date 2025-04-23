class Node:
    """
este nodo contiene la ccion del editor de texto, donde cada nodo conce la accion

    """
    def __init__(self, data):
        self.data = data      # Acción que representa este nodo 
        self.prev = None          # Nodo previo
        self.next = None          # Nodo siguiente
