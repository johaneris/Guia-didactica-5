class Paciente:
    def __init__(self, nombre: str, edad: int, sintoma: str, prioridad: int):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma
        self.prioridad = prioridad

class Node:
    def __init__(self, pacient):
        self.next = None
        self.pacient = pacient
        
class RegistroPaciente:
    def __init__(self):
        self.head = None
        
    def append(self, nombre: str, edad: int, sintoma: str, prioridad: int):
        new_node = Node(Paciente(nombre, edad, sintoma, prioridad))
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def show_patients(self):
        if not self.head:
            print("No hay pacientes registrados...")
            return
    
        temp = self.head
        while temp:
            print(f"Nombre: {temp.pacient.nombre}\nSintoma: {temp.pacient.sintoma}\nPrioridad: {temp.pacient.prioridad}", end="\n\n")
            temp = temp.next
    
    def attend_patients(self):
        if not self.head:
            print("No hay pacientes registrados...")
            return

        for priority in range(5, 0, -1):
            temp = self.head
            prev = None

            while temp:
                if temp.pacient.prioridad == priority:
                    print("╔═══════════════════════════════════════════════════════╗")
                    print("║Atendiento")
                    print(f"║Paciente: {temp.pacient.nombre}")
                    print(f"║Prioridad: {temp.pacient.prioridad}")
                    print("╚═══════════════════════════════════════════════════════╝")

                    if prev:
                        prev.next = temp.next
                    else:
                        self.head = temp.next

                    return
                prev = temp
                temp = temp.next
        
        print("No hay pacientes registrados...")