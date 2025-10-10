# # CLASE 10/10/2025

# # INPUT
# nombre = input("¿Cómo te llamas? ")
# print(f"Hola mi nombre es {nombre}")

# # INT : convertimos a entero. Tenemos que tener cuidado, cuando escribirmos un número es un str, importante convertirlo a int
# texto_entero = input("Introduce un número ")
# numero_entero = int(texto_entero)
# print(type(texto_entero))
# print(type(numero_entero))

# # Ejercicio de prueba
# a= input("Introduce un número ")
# b= input("Introduce otro número ")
# print(int(a)+int(b)) # Si no convertimos a int, concatena los dos str
# print(a+b)

# # # FLOAT : convertimos a decimal
# texto_decimal = "3.14159"
# numero_decimal = float(texto_decimal)
# print(type(texto_decimal))
# print(type(numero_decimal))

# # ROUND : redondea un número decimal al número par más cercano. Esto se hace para evitar sesgos en los cálculos estadísticos.
# print(round(3.14159))  
# print(round(2.7))
# print(round(2.5))    
# print(round(3.5)) 
# print(round(3.14159, 2))

# # CONTROL DE FLUJO

# Break: rompe el bucle y sale de él

# numeros = [1, 5, 8, 12, 15, 20]
# numero_objetivo = 12
# for num in numeros:
#     print(f"Comprobando el número: {num}")
#     if num == numero_objetivo:
#         print(f"¡Encontrado! El número {numero_objetivo} está en la lista.")
#         break  #Sale del bucle 'for' inmediatamente

# print(f"El número {num} no es el objetivo.")
# print("Fin del programa después del bucle.")


# # Continue: salta a la siguiente iteración del bucle

# numeros = [1, 2, 3, 4, 5, 6, 7]
# for num in numeros:
#     if num % 2 == 0: 
#         print(f"Saltando el número par: {num}")
#         continue   
#     print(f"Procesando número impar: {num} (su cuadrado es {num * num})")

# print("Fin del programa después del bucle.")

# Ejercicio: Filtrado de Edades en una Lista
# lista_edades=[15, 22, 17, 30, 65, 45, 70, 19]

# print("Forma1:")
# for edad in lista_edades:
#     if edad > 18 and edad < 65:
#         print(f"Edad {edad} es mayor de edad.")
#     elif edad >= 65:
#         print(f"Ejecución detenida por edad avanzada.")
#         break

# print("Forma2:")   
# # Cuando queramos parar ponerlo lo primero 
# for edad in lista_edades:
#     if edad >= 65:
#         print(f"Ejecución detenida por edad avanzada ", edad)
#         break       
#     elif edad >= 18:
#         print(f"Edad {edad} es mayor de edad.")
        
# print("Forma3:")   
# # Este código no funciona correctamente porque nos muestra el de 65
# for edad in lista_edades:
#     if edad >= 18:
#         print(f"Edad {edad} es mayor de edad.")
#     elif edad >= 65:
#         print(f"Ejecución detenida por edad avanzada ", edad)
#         break
    

# # Try / Except: si ocurre un error nos ejecuta la parte de except (localizar errores)
# try:
#     resultado = 10 / 0
# except:
#     print("Error!!")

# Practica: utiliza lo aprendido hasta ahora

# Forma 1
# contador = 1
# while contador < 6:
#     a= input("Introduce un número ")
#     try:
#         if a.isdigit():
#             a= int(a)
#             print(f'El numero es válido {a} y es de tipo {type(a)}, numero de intentos {contador}')
#             break 
#         else:
#             print(f'No es un dígito, numero de intentos {contador}')
#             contador += 1
#     except:
#         print('Error')
        
# Forma 2:
# intento = 1
# while intento <= 5:
#     try:
#         numero = int(input("Introduzca un número"))
#         print("El número es válido")
#         break
#     except:
#         print("Esto no es un número")
#     intento += 1

# Forma 3:
# contador = 1
# while contador < 6:
#     a = input("Introduce un número: ")
#     try:
#         a = int(a)  # Intentamos convertir directamente
#         print(f"El número es válido: {a}, tipo: {type(a)}, intento {contador}")
#         break
#     except ValueError:
#         print(f"Error: '{a}' no es un número válido. Intento {contador}")
#     contador += 1


# # PROGRAMACION ORIENTADA A OBJETOS

# Repaso diccionarios 

# mianimal1 ={
#     "nombre":"Sasu",
#     "edad":1
# }
# mianimal2 ={
#     "nombre":"Neva",
#     "edad":2
# }
# mianimal3 ={
#     "nombre":"Simba",
#     "edad":1
# }

# print(mianimal1["nombre"])

# # Repaso diccionarios 

# numeros= [1,2,3]
# print(numeros[2])


# # Definición de clases : En vez de crear varios diccionarios creamos una clase.

# Clase 1:
# self: referencia al objeto que estoy creando
# class Animal: # en nombre de la clase la primera letra en mayúscula
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
    
#     def hacer_sonido(self): # una función que esta dentro de una clase se le llama método
#         print("El animal hace un sonido genérico.")


# mi_animal4 = Animal("Fido", 5) # creamos una instancia de la clase animal
# mi_animal5 = Animal("Salva", 22)
# mi_animal6 = Animal("Neva", 2)

# print(f"Mi animal se llama {mi_animal6.nombre} y tiene {mi_animal6.edad} años.")
# mi_animal6.hacer_sonido()

# Clase 2:
# cls : hace referencia a la clase entera
# class Empleado:
#     sueldo_base = 50000 # propiedad 
    
#     def __init__(self, nombre, cargo):
#         self.nombre = nombre
#         self.cargo = cargo
    
#     @classmethod # utilizar este método cuando hemos definido una variable en la clase
#     def aumentar_sueldo_base(cls):
#         cls.sueldo_base += 1000
#         print(f"El nuevo sueldo base es: {cls.sueldo_base}")
        
# empleado1 = Empleado("Ana", "Gerente")
# print(f"Sueldo de {empleado1.nombre}: {Empleado.sueldo_base}")

# Empleado.aumentar_sueldo_base() # aumentamos el sueldo a todos los empleados creados despues el sueldo
# empleado2 = Empleado("Juan", "Peon")
# print(f"Sueldo de {empleado1.nombre}: {Empleado.sueldo_base}")


# Clase 3:
# class Matematica:
#     @staticmethod
#     def sumar(a, b):
#         return a + b
    
#     @staticmethod
#     def restar(a, b):
#         return a - b
    
#     @staticmethod
#     def multiplicar(a, b):
#         return a * b

# print(Matematica.sumar(5, 3))

# Ejercicio:el nombre de la clase en mayusculas y cuando creamos un objeto en minusculas

# class Producto:
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio
    
#     def mostrarDetalles(self): # importante poner self en la creación del método
#         print(f"El producto {self.nombre} tiene de precio {self.precio}")

# producto1= Producto('Ordenador','1000') 
# producto2 = Producto('Movil','2000')

# producto1.mostrarDetalles()
# producto2.mostrarDetalles() 

# # HERENCIA: creamos una clase hija a partir de una clase que ya hemos creado (de esta forma no repetimos el codigo)

# class Animal: 
#     def __init__(self, nombre):
#         self.nombre = nombre
    
#     def hacer_sonido(self):
#         print("El animal hace un sonido genérico.")

# class Perro(Animal): # creamos una clase hija 
#     def __init__(self, nombre, raza): # añadimos las mismas propiedades + las propiedades de la nueva clase
#         super().__init__(nombre) # llamamos a las propiedades de la clase padre
#         self.raza = raza # y ya luego añadimos las nuevas propiedades
        
#     # def hacer_sonido(self): # podemos sobreescribir el método de la clase padre o crear directamente un metodo nuevo
#     #     print("El perro ladra: ¡Guau!")
        
#     def hacer_sonido(self): 
#         super().hacer_sonido() # me mantiene el código del método padre 
#         print("Esto es el metodo del perro")

# animal_generico = Animal("Tommy")
# animal_generico.hacer_sonido() 
# perro = Perro("Tommy","husky")
# perro.hacer_sonido()


# Ejercicio

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrarDetalles(self): # importante poner self en la creación del método
        print(f"El producto {self.nombre} tiene de precio {self.precio}")
        
class Electrodomestico(Producto):
    def __init__(self, nombre, precio, marca):  # truco: si pones __init__ te deja seleccionar la opcion para que te deje crear todo
        super().__init__(nombre, precio) 
        self.marca = marca 
        
    def encender(self):
        print("Encendiendo...")
    

producto1= Producto('Ordenador','1000') 
producto2 = Producto('Movil','2000')
producto1.mostrarDetalles()
producto2.mostrarDetalles() 

producto3 = Electrodomestico("IPAD","3000","APPLE")
producto3.mostrarDetalles()
producto3.encender()














