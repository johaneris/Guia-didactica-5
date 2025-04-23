class Nodo:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, estudiante):
        nuevo_nodo = Nodo(estudiante)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def ordenar_por(self, opcion_campo):
        if self.cabeza is None:
            return
        
        cambiado = True
        while cambiado:
            cambiado = False
            actual = self.cabeza
            while actual.siguiente:
                a = self.obtener_valor_campo(actual.estudiante, opcion_campo)
                b = self.obtener_valor_campo(actual.siguiente.estudiante, opcion_campo)
                if str(a).lower() > str(b).lower():
                    actual.estudiante, actual.siguiente.estudiante = actual.siguiente.estudiante, actual.estudiante
                    cambiado = True
                actual = actual.siguiente

    def obtener_valor_campo(self, estudiante, opcion):
        if opcion == 1:
            return estudiante.carnet
        elif opcion == 2:
            return estudiante.nombres
        elif opcion == 3:
            return estudiante.apellidos
        elif opcion == 4:
            return estudiante.peso
        elif opcion == 5:
            return estudiante.estatura
        elif opcion == 6:
            return estudiante.sexo
        elif opcion == 7:
            return estudiante.promedio
        else:
            return ""

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.estudiante)
            actual = actual.siguiente