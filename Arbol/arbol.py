
# Arbol Binario de Busqueda (ABB)

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self):
        self.raiz = None

    # Insertar numeros
    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)

        return nodo

    # Buscar un numero
    def buscar(self, nodo, valor):
        if nodo is None:
            return False

        if nodo.valor == valor:
            return True

        if valor < nodo.valor:
            return self.buscar(nodo.izquierda, valor)
        else:
            return self.buscar(nodo.derecha, valor)

    # Recorrido preorden
    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    # Recorrido inorden
    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecha)

    # Recorrido postorden
    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.valor, end=" ")


# Crear el arbol
arbol = Arbol()

# Insertar valores
numeros = [50, 30, 70, 20, 40, 60, 80]

for numero in numeros:
    arbol.insertar(numero)

# Mostrar recorridos
print("Recorrido Preorden:")
arbol.preorden(arbol.raiz)

print("\nRecorrido Inorden:")
arbol.inorden(arbol.raiz)

print("\nRecorrido Postorden:")
arbol.postorden(arbol.raiz)

# Buscar un numero
numero_buscar = 40

print("\n\nBuscar numero:", numero_buscar)

if arbol.buscar(arbol.raiz, numero_buscar):
    print("El numero existe en el arbol")
else:
    print("El numero no existe en el arbol")
