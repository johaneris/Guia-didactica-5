from paquetes.listaenlazada import LinkedList

def main():
    """
    Función principal que muestra un menú interactivo para que el usuario
    pueda agregar acciones, deshacer, rehacer y ver el historial de acciones.
    """
    history = LinkedList()  # Se crea una nueva lista enlazada para el historial

    while True:
        print("\nOpciones:")
        print("1. Agregar acción")
        print("2. Deshacer")
        print("3. Rehacer")
        print("4. Ver historial")
        print("5. Salir")

        choice = input("Seleccione una opción: ")  # Leer opción del usuario

        if choice == "1":
            action = input("Ingrese la acción (write, delete, copy, etc.): ")
            history.Agregar_Accion(action)  # Agrega la acción ingresada al historial
        elif choice == "2":
            history.undo()              # Llama a la función deshacer
        elif choice == "3":
            history.redo()              # Llama a la función rehacer
        elif choice == "4":
            history.imprimir()      # Muestra todo el historial de acciones
        elif choice == "5":
            print("Saliendo del programa.")
            break                       # Sale del ciclo y finaliza el programa
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

        