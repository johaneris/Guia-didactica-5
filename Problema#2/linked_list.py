class Station:
    def __init__(self, nombre, tiempo_siguiente):
        self.nombre = nombre
        self.tiempo_siguiente = tiempo_siguiente
        
class Node:
    def __init__(self, station):
        self.data = station
        self.next = None
        
class Ruta:
    def __init__(self):
        self.head = None
        
    def append(self, nombre: str, tiempo_siguiente: int):
        new_node = Node(Station(nombre, tiempo_siguiente))
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def print_stations(self):
        if not self.head:
            print("No hay estaciones registradas...")
            return
        temp = self.head
        while temp:
            print(temp.data.nombre, end=" -> ")
            temp = temp.next
        print("Final")
        
    def expected_time(self, origin, destiny):
        stations = []
        temp = self.head
        # guardar estaciones em una lista
        while temp:
            stations.append(temp)
            temp = temp.next
            
            
        # Guardar nombre de estaciones de la lista "stations"
        names_stations = [e.data.nombre for e in stations]
        
        
        # Determinar si se encuentran el origen y el destino
        if origin not in names_stations or destiny not in names_stations:
            print("Estacion no registrada...")
            return
        
        # Tomar el index de la lista de names_stations
        index_origin = names_stations.index(origin)
        index_destiny = names_stations.index(destiny)
        
        
        # Determinar si el origen es el destino
        if index_origin == index_destiny:
            print("Ya se encuentra en la estacion destinada")
            return
                  
        # Calcular el tiempo de estimado (elementos de izquierda a derecha)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        expected_time = 0
        if index_origin < index_destiny:
            for i in range(index_origin, index_destiny):
                expected_time += stations[i].data.tiempo_siguiente
        elif index_origin > index_destiny:
            # Calcular el tiempo de estima (elementos de derecha a izquierda)
            for i in range(index_destiny, index_origin):
                expected_time += stations[i].data.tiempo_siguiente
        print(f"Desde la estacion {origin}, hasta la estacion {destiny}")
        print(f"Tiempo estimado: {expected_time} minutos.")