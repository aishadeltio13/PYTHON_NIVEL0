# # DIA 27/09/2025

# PRACTICA 1:

persona = {
    "nombre": "Sofía",
    "edad": 20,
    "altura": 1.78,
    "hobbies": ["leer","fútbol","motociclismo"]
}


if type(persona) == dict: #estamos mirando si persona es un diccionario (tipo de variable)
    print("apruebas 1")
else:
    print("suspendes 1")


if persona["nombre"] == "Sofía":
    print("apruebas 2")
else:
    print("suspendes 2")

if persona["edad"] >= 18:
    print("apruebas 3")
else:
    print("suspendes 3")
    
if type(persona["altura"]) == float:
    print("apruebas 4")
else:
    print("suspendes 4")
    
if persona["hobbies"][1] == "fútbol":
    print("apruebas 5")
else:
    print("suspendes 5")

# PRACTICA 2:

pruebaDicc ={
    "x":7,
    "y":"hola",
    "a" :{"b":3},
    "z":[1,2,"tres"]
}

if type(pruebaDicc) == dict:
	print("apruebas 1")
else:
	print("suspendes 1")
 
if pruebaDicc["x"] == 7:
	print("apruebas 2")
else:
	print("suspendes 2")
 
if pruebaDicc["y"] =="hola":
    print("apruebas3")
else:
    print("suspendes3")

if pruebaDicc["a"]["b"] == 3: # accedemos a la propiedad a de un diccionario. En donde dentro del diccionario a hay otro diccionario b.
    print("apruebas 4")
else:
    print("suspendes 4")

if pruebaDicc["z"][1] == 2: #accedemos a la propiedad z de un diccionario. Y accedemos a la posicion 1 de la lista que hay dentro de z.
    print("apruebas 5")
else:
    print("suspendes 5")
    
if type(pruebaDicc["z"][2]) == str:
    print("apruebas 6")
else:
    print("suspendes 6")
    
# PRACTICA 3:

frutas = ["peras","fresas",{"verduras":"lechuga"}]
print(frutas[2]["verduras"]) # accedemos a la posicion 2 de la lista frutas, que es un diccionario. Y dentro de ese diccionario accedemos a la propiedad verduras.

# PRACTICA BUCLE FOR, WHILE:

vueltas = [1,2,3,4,5,6,7,8]

for circuito in vueltas:
	print(f'Esta es la vuelta nº {circuito}')
 
nombre = ["Luffy", "Nami", "Pedro"]
print(nombre[1])
print(nombre[2])

for persona in nombre:
    print(f'Hola {persona}')

vueltas = [1,2,3,4,5,6,7,8]

contador = 0
while contador <= 5:
	print(f"Estoy en la vuelta {vueltas[contador]}")
	contador += 1 #contador = contador + 1
 
 
# PRACTICA 4

productos = [
  {"nombre": "Laptop", "categoria": "Electrónica", "precio": 799.99, "stock": 25},
  {"nombre": "Auriculares Bluetooth", "categoria": "Accesorios", "precio": 59.99, "stock": 50},
  {"nombre": "Cámara Digital", "categoria": "Fotografía", "precio": 399.99, "stock": 10},
  {"nombre": "Smartwatch", "categoria": "Relojes", "precio": 149.99, "stock": 75},
  {"nombre": "Teclado Mecánico", "categoria": "Accesorios", "precio": 89.99, "stock": 30}
 ]

print(productos[0]["nombre"]) # accedemos a la posicion 0 de la lista productos, que es un diccionario. Y dentro de ese diccionario accedemos a la propiedad nombre.


print("Muestra por consola el nombrede cada producto (bucle for)") # En bucle for no hace falta poner contador porque lo hace automatico 
for elemento in productos:
    print(elemento["nombre"])

   
print("Muestra por consola el nombre de cada producto (bucle while)")
contador = 0
while contador < len(productos):
    print(productos[contador]["nombre"])
    contador += 1

print("Muestra por consola el nombre de cada product cuyo precio es mayor a 100.")
for elemento in productos:
    if elemento["precio"] > 100:
        print(elemento["nombre"])
    
        
print("Muestra por consola el nombre de los productos cuyo stock es menor o igual a 25")
for elemento in productos:
    if elemento["stock"] <= 25:
        print(elemento["nombre"])
    

# FUNCIONES

#Lo que entra en la funcion debe de ir en parentesis
def suma_func(a, b):  
    return a + b

c = suma_func(2, 2)
d = suma_func(8, 8)

suma = [c, d]
contador = 0
for numero in suma:
    print('El resultado de la operacion ' + str(contador) + ' es ' + str(suma[contador]))
    contador += 1


def frase():
    return "Esto es una frase"
print(frase())

def mostrarNombre(nombre):
    return nombre
print(mostrarNombre("Aisha"))


def saludar(nombre):
    return f"Hola {nombre}" # f es para formatear la cadena y que reconozca las variables dentro de {}

print(saludar("Aisha")) 


def greet(name, greeting="Hello"): # greeting es un parametro opcional, si no se le pasa ningun valor, por defecto sera "Hello"
    if not name:
        return greeting
    else:
        return f"{greeting} {name}"

print(greet("Sofía"))      
print(greet("Sofía", "Hola"))  
print(greet("")) 


# PRACTICA 

def cuentaCaracteres(palabra):
    if type(palabra) == str:
        return f'La palabra {palabra} tiene {len(palabra)} caracteres'
    return "Debo ser ejecutada con un string"

print(cuentaCaracteres("Hola Mundo")) # 10
print(cuentaCaracteres(7)) # Error  


def sumar_dos(x):
    return x+2

numero=5
numero=sumar_dos(numero) # Se actualiza el valor de numero
print(numero)


mi_lista = ["uno", "dos"]
print(mi_lista)
def agregar_elemento(lista):
    lista.append("nuevo")
    
agregar_elemento(mi_lista)
print(mi_lista)

# Argumentos posicionales y no posicionales
def saludar(nombre, apellido):
    print(f"Hola, {nombre} {apellido}")
saludar("Juan", "Pérez")
saludar("Pérez", "Juan")

def configurar_usuario(nombre, edad, activo=True): # activo es un parametro opcional, si no se le pasa ningun valor, por defecto sera True
  print(f"Usuario: {nombre}, Edad: {edad}, Activo: {activo}")
  
configurar_usuario(nombre="María", edad=25) # Si escribo el nombre de la variable, no importa el orden


def mostrar_info(id_producto, nombre, precio, descuento=0):
    print(f"ID: {id_producto}, Nombre: {nombre}, Precio: {precio}, Descuento: {descuento}")

mostrar_info(101, "Camiseta", descuento=0.1, precio=25) # Cuando mezclamos argumentos posicionales y no posicionales, los posicionales deben ir primero

def sumar_todos(*numeros): # el asterisco indica que puede recibir cualquier numero de argumentos y los agrupa en una tupla
    print(f"Tipo de 'numeros': {type(numeros)}")
    total = 0

    for num in numeros:
        total += num # total = total + num
    return total

print(sumar_todos(1, 2, 3))     
print(sumar_todos(50, 20, 30, 40, 10 )) 
print(sumar_todos(5))  

persona={
    "nombre": "Luis",
    "edad": 28,
}
print(persona.items())
print(persona.keys())
print(persona.values())

def configurar_perfil(**opciones_perfil): # el doble asterisco indica que puede recibir cualquier numero de argumentos nombrados y los agrupa en un diccionario
    print(f"Tipo de 'opciones_perfil': {type(opciones_perfil)}") 
    print("Configuración del perfil:")
    for a, b in opciones_perfil.items():
        print(f" {a}: {b}")
        
configurar_perfil(nombre="Ana", edad=30, ciudad="Valencia")
configurar_perfil(tema="oscuro", notificaciones=True) 

def procesar_datos(identificador, *valores, **opciones):
    print(f"Identificador: {identificador}")
    print(f"Valores adicionales (tupla): {valores}")
    print(f"Opciones (diccionario): {opciones}")


procesar_datos("producto_A", 10, 20, 30, color="rojo", tamaño="grande")

# FUNCIONES LAMBDA: se utilizan para funciones pequeñas de una sola linea
suma_l = lambda x, y: x + y # es como si estuviera haciendo return x + y
print(f'El resultado es {suma_l(5, 3)}')

primera_letra= lambda x: x[0]
x= "AISHA"
print(f'La primera letra de la palabra {x} es {primera_letra(x)}')


# PROBAR DE BUGGER
def obtener_nombre_completo(nombre, apellido):
    return nombre + " " + apellido

def main():
    usuarios = [
        {"nombre": "Sofía"},
        {"nombre": "Luis", "apellido": "Martínez"},
    ]
   
    for usuario in usuarios:
        if "nombre" in usuario and "apellido" in usuario:
            completo = obtener_nombre_completo(usuario["nombre"], usuario["apellido"])
            print(completo)
        elif "nombre" in usuario:
            print(f"Falta el apellido para {usuario['nombre']}")
        else:
            print("Faltan datos, llamar a administracion")

main()







