from dataclasses import dataclass

#clase Elemento usando el decorador @dataclass 
@dataclass
class Elemento:
    nombre: str #atributo

#método especial para soportar la operación de igualdad ==
    def __eq__(self, comparar): 
        if isinstance(comparar, Elemento):
            return self.nombre == comparar.nombre
        return False
    
#clase Conjunto definida
class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.elementos = [] #atributo inicializado como lista vacia
        self.nombre = nombre # atributo nombre del conjunto
        self.__id = Conjunto.contador #atributo de clase contador lleva registro del número de instancias creadas
        Conjunto.contador += 1

    @property
    def id(self): # atributo “privado” __id al cual se le asigna el valor actual del atributo de clase contador 
        return self.__id

    def contiene(self, elemento): # método de instancia contiene
        return any(e == elemento for e in self.elementos) # valor bool indicando si el conjunto contiene ya un elemento con el mismo nombre

    def agregar_elemento(self, elemento): # método de instancia agregar_elemento
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto): # método unir 
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto): #  agrega sus elementos a la lista de elementos del objeto actual 
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO A {otro_conjunto.nombre}")
        nuevo_conjunto.elementos = self.elementos.copy()
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2): #método de clase intersectar 
        nuevo_nombre = f"{conjunto1.nombre} INTERSECTADO CON {conjunto2.nombre}"
        elementos_interseccion = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
        nuevo_conjunto = Conjunto(nuevo_nombre)
        nuevo_conjunto.elementos = elementos_interseccion
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join(e.nombre for e in self.elementos)
        return f"Conjunto del  {self.nombre}: ({elementos_str})"

# Crear elementos
elemento1 = Elemento("E1")
elemento2 = Elemento("E2")
elemento3 = Elemento("E3")

# Crear conjuntos
conjunto1 = Conjunto("Grupo1")
conjunto2 = Conjunto("Grupo2")

# Agregar elementos a los conjuntos
conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)

conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

# Unir conjuntos
conjunto3 = conjunto1 + conjunto2

# Intersectar conjuntos
conjunto4 = Conjunto.intersectar(conjunto1, conjunto2)

# Imprimir conjuntos
print(conjunto1)
print(conjunto2)
print(conjunto3)
print(conjunto4)
