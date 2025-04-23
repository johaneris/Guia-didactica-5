from linked_lisy import RegistroPaciente

def menu():
    patients: RegistroPaciente = RegistroPaciente()
    while True:
        print("1. Agregrar Pacientes ")
        print("2. Mostrar Pacientes ")
        print("3. Atender Pacientes ")
        print("4. Salir")
        opc = input("Elija una opcion: ")
        match opc:
            case "1":
                try: 
                    nombre = input("Ingrese el nombre del paciente: ")
                    edad = int(input("Ingrese la edad del paciente: "))
                    sintoma = input("Ingrese el sintoma del paciente: ")
                    while True:
                        prioridad = int(input("Ingrese la prioridad del paciente (1 - 5): "))
                        if prioridad in range(1, 5):
                            break
                    patients.append(nombre, edad, sintoma, prioridad)
                except Exception:
                    print("No se han ingresado correctamente los datos...")
            
            case "2":
                patients.show_patients()
                
            case "3":
                patients.attend_patients()
                
            case "4":
                print("Saliendo....")
                break
            case _:
                print("Opción inválida, intente nuevamente...")