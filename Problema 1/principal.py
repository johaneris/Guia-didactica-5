"""
Problema#1
Una escuela de educación primaria requiere un algoritmo que muestre los datos de los
estudiantes de un salón de clase ordenados de forma ascendente, según un parámetro
indicado; este parámetro puede ser cualquie
"""

from clase_estudiante import Estudiante
from nodo_listaEnlazada import ListaEnlazada

def main():
    lista = ListaEnlazada()

    while True:
        print("\n«« MENÚ PRINCIPAL »»")
        print("1. Agregar estudiante")
        print("2. Mostrar lista ordenada por un campo")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\nRegistro de Estudiante")
            carnet = input("Carnet: ")
            nombres = input("Nombre: ")
            apellidos = input("Apellido: ")
            peso = float(input("Peso (kg): "))
            estatura = float(input("Estatura (m): "))
            sexo = input("Genero (M/F): ")
            promedio = float(input("Promedio: "))
            estudiante = Estudiante(carnet, nombres, apellidos, peso, estatura, sexo, promedio)
            lista.insertar(estudiante)
            print("Estudiante agregado con éxito.")

        elif opcion == '2':
            print("\n--- CAMPOS DISPONIBLES PARA ORDENAR ---")
            print("1. Carnet")
            print("2. Nombres")
            print("3. Apellidos")
            print("4. Peso")
            print("5. Estatura")
            print("6. Genero")
            print("7. Promedio")
            campo = int(input("Seleccione el número del campo para ordenar: "))

            if campo >= 1 and campo <= 7:
                lista.ordenar_por(campo)
                print("\nLista ordenada:\n")
                lista.mostrar()
            else:
                print("Campo inválido, intente nuevamente.")

        elif opcion == '3':
            print("Ha salido del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main()