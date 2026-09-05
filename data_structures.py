# 1. ESTRUCTURAS DE DATOS DE MEMORIA (Nodos, Lista, Pila, Cola)

class Nodo:
    """Clase base para construir estructuras enlazadas."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    """Para el Catálogo de Recetas y SubRecetas."""
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def agregar(self, dato):
        """Agrega un elemento al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamano += 1

    def __iter__(self):
        """Permite iterar sobre los elementos de la lista."""
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

    def obtener_tamano(self):
        """Retorna el tamaño de la lista."""
        return self.tamano


class Pila:
    """Estructura LIFO para el Historial de recetas vistas o acciones."""
    def __init__(self):
        self.tope = None
        self._tamano = 0

    def apilar(self, dato):
        """Agrega un elemento al tope de la pila (push)."""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self._tamano += 1

    def desapilar(self):
        """Extrae el elemento del tope de la pila (pop)."""
        if self.es_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self._tamano -= 1
        return dato

    def es_vacia(self):
        """Verifica si la pila está vacía."""
        return self.tope is None

    def obtener_tamano(self):
        """Retorna el tamaño de la pila."""
        return self._tamano


class Cola:
    """Estructura FIFO para la Cola de Preparación / Turnos de Cocina."""
    def __init__(self):
        self.frente = None
        self.final = None
        self._tamano = 0

    def encolar(self, dato):
        """Agrega un elemento al final de la cola (enqueue)."""
        nuevo_nodo = Nodo(dato)
        if self.es_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self._tamano += 1

    def desencolar(self):
        """Extrae el primer elemento de la cola (dequeue)."""
        if self.es_vacia():
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self._tamano -= 1
        return dato

    def es_vacia(self):
        """Verifica si la cola está vacía."""
        return self.frente is None

    def obtener_tamano(self):
        """Retorna el tamaño de la cola."""
        return self._tamano
