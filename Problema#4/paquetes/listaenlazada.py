from paquetes.node import Node 

class LinkedList:

    """lista doblemente enlazada que almacena el historial de las acciones
    que tiene el editor de tecto, en este se puede navegr hacia 
    adelante y hacia atras"""

    def __init__(self):
        self.head = None #rpresenta el primer nodo del historial
        self.tail = None #ultimo nodo del historial
        self.current = None # Nodo actual, es donde el usuario ha lelgado 

    def Agregar_Accion(self, data):

        "nodo al historial"
        new_node = Node(data)

        #si no se han ingresados acciones , se inicializa todooo

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else: 
            # si el usuario usa la funcion undo entonces se devielde
            #entonces loqe le sigue se elimina, las acciones futuras
            if self.current != self.tail:
                self.current.next = None # le die que al final va a ser None, que es como romper un vinculo con el siguiente noso
                self.tail = self.current #actualizo el final de la lista (HERE )
            #se conext el nuevo nodo al final de la lista 
            self.tail.next = new_node # el nodo actial apunta al nuevo nodo como el sig

            new_node.prev = self.tail #esto es ocomo decir que vio despues del siguiente  asi que es el prev 
            #hayq ue amrcar el siguiente nodocoo el que esta el usuario ahora
            self.tail =new_node
            self.current = new_node
        
        print(f"Se agrego {data} al historial")


    def undo(self):
        '''retoede una accion en el historial si es posible
        es decriq eue el current semueve pa atras 
        '''

        if self.current is not None:
            #mostrar que accion se real
            print(f"Deshacer la accion: {self.current.data}")
            #solo s epuede retroceder si hay un nodo anterior al actua

            if self.current.prev is not None:
                self.current = self.current.prev
                '''aqyi el currente se va a la accion previa en el historial'''
            else:
                print("ya no hay mas para deshcer")

    def redo(self):
        '''rehacer la accion previamente deshecha, mueve a current hacia adelante si ahy algo
        '''
        if self.current is not None and self.current.next is not None:
            self.current = self.current.next
            print(f"rehacer la accion: {self.current.data}")
        else:
            print("No hay acciones para rehacer")

    def imprimir(self):
        print("Historial de acciones:")

        nodo_actual = self.head  # Empezamos desde el primer nodo
        while nodo_actual:
            es_actual = ""
            if nodo_actual == self.current:
                es_actual = "<- actual"
            print(f"- {nodo_actual.data} {es_actual}")
            nodo_actual = nodo_actual.next







