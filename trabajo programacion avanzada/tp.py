#Ejercicio 2
class Punto :
 def __init__(self, x, y):
     self._x = x
     self._y = y
     
     
     
 def eje_x(self):
     
     return self.x 
 
 
 def eje_y(self):
     
     return self.y 
 
 
 
 def impresion(self):
     
     return f'Punto({self.x},{self.y})'
 
 
 def opuesto(self):
     
     return Punto(-self.x, -self.y)
 
 
 def distancia_al_origen(self):
     
     return (self.x2 + self.y2)**0.5




#Ejercicio 3
class Linea : 
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b
        
        
def mueve_derecha(self):
    self._punto_a.mover_x(distancia)
    self._punto_b.mover_x(distancia)
    
def mueve_izquierda(self, distncia):
    self._punto_a.mover_x(-distncia)
    self._punto_b.mover_x(-distncia)
    
def mueve_arriba(self, distancia):
    self._punto_a.mover_y(distancia)
    self._punto_b.mover_y(distancia)
    
def mueve_abajo(self, distancia):
    self._punto_a.mover_y(-distancia)
    self._punto_b.mover_y(-distancia)
    



#Ejercicio 4
class Cancion:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

def get_titulo(self):
    return self._titulo

def get_autor(self):
    return self._autor

def set_titulo(self):
    self._titulo = titulo
    
def set_autor(self):
    self._autoir = autor
        
    
    
        
#Ejercicio 5
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido
        
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Libro:
    def __init__(self, titulo, autor, ISBN, paginas, edicion, editorial, lugar, fecha_emdicion):
        self._titulo = titulo
        self._autor = autor
        self._ISBN = ISBN
        self._paginas = paginas
        self._edicion = edicion
        self._editorial = editorial
        self._lugar = lugar
        self._fecha_edicion = fecha_emdicion
    
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_ISBN(self):
        return self.ISBN
    def get_paginas(self):
        return self.paginas
    def get_edicion(self):
        return self.edicion
    def get_editorial(self):
        return self.editorial
    def get_lugar(self):
        return self.lugar
    def get_fecha_emicion(self):
        return self.fecha_edicion
    
    
    def set_titulo(self, titulo):
         self = titulo
    
    def set_autor(self, autor):
        self = autor
    
    def set_isbn(self, isbn):
        self = isbn
    
    def set_paginas(self, paginas):
        self = paginas
        
    def set_edicion(self,edicion):
        self = edicion
    
    def set_editorial( self, editorial):
        self = editorial
    
    def set_lugar(self, lugar):
        self = lugar
    
    def set_fecha_edicion(self, fecha_edicion):
        self = fecha_edicion


def leer_informacion(self):
    self.titulo = input("ingrese el titulo del libro:")
    nombre_autor = input("ingrese el nombre del autor:")
    apellido_autor = input("ingrese el apellido del autor:")
    self.autor = Persona (nombre_autor, apellido_autor)
    self.isbn = input("ingrese el isbn del libro")
    self.paginas = int(input("ingrese el numeri de paginas en el libro:"))
    self.edicion = input("ingrese la edicion:")
    self.editorial = input("ingrese la editorial:")
    ciudad = input("ingrese la ciudad del lugar:")
    pais = input("ingrese el pais del lugar:")
    self.lugar = (ciudad, pais)
    self.fecha_edicion = input("ingrese la fecha de emicion:")
    
    def mostrar_informacion(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: [self.isbn]")
        print(f"Paginas: {self.paginas}")
        print(f"Edicion: {self.edicion}")
        print(f"Editorial: {self.editorial}")
        print(f"Lugar: {self.lugar[0]},{self.lugar[1]}")   
        print(f"Fecha de edicion: {self.fecha_edicion}")
        
    
 