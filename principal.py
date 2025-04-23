class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nodo = Nodo(dato)
        nodo.siguiente = self.cabeza
        self.cabeza = nodo

    def insertar_final(self, dato):
        nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía.")
            return
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("fin")

    def buscar(self, valor):
        actual = self.cabeza
        indice = 0
        while actual:
            if actual.dato == valor:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1

    def actualizar(self, indice, nuevo_valor):
        actual = self.cabeza
        pos = 0
        while actual and pos < indice:
            actual = actual.siguiente
            pos += 1
        if actual:
            actual.dato = nuevo_valor
            return True
        return False

    def eliminar_inicio(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def eliminar_final(self):
        if not self.cabeza:
            return
        if not self.cabeza.siguiente:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente:
                actual = actual.siguiente
            actual.siguiente = None

def main():
    lista = ListaEnlazada()

    # Cargar datos iniciales
    for valor in [10, 15, 20, 26, 30, 39]:
        lista.insertar_final(valor)

    print("Lista inicial:")
    lista.imprimir()

    # Menú interactivo
    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Buscar un valor")
        print("4. Actualizar un valor por índice")
        print("5. Eliminar el primer elemento")
        print("6. Eliminar el último elemento")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            dato = int(input("Dato a insertar al inicio: "))
            lista.insertar_inicio(dato)
            print("Dato insertado al inicio. Lista actual:")
            lista.imprimir()

        elif opcion == "2":
            dato = int(input("Dato a insertar al final: "))
            lista.insertar_final(dato)
            print("Dato insertado al final. Lista actual:")
            lista.imprimir()

        elif opcion == "3":
            valor = int(input("Valor a buscar: "))
            indice = lista.buscar(valor)
            if indice != -1:
                print(f"Valor encontrado en el índice {indice}")
            else:
                print("Valor no encontrado.")
            print("Lista actual:")
            lista.imprimir()

        elif opcion == "4":
            indice = int(input("Índice a actualizar: "))
            nuevo_valor = int(input("Nuevo valor: "))
            if lista.actualizar(indice, nuevo_valor):
                print("Valor actualizado.")
            else:
                print("Índice fuera de rango.")
            print("Lista actual:")
            lista.imprimir()

        elif opcion == "5":
            lista.eliminar_inicio()
            print("Primer elemento eliminado. Lista actual:")
            lista.imprimir()

        elif opcion == "6":
            lista.eliminar_final()
            print("Último elemento eliminado. Lista actual:")
            lista.imprimir()

        elif opcion == "7":
            print("Ha salido del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
