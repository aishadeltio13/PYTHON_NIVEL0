# EJERCICIO 1
# Crea una función que convierta un str en un número. Si el argumento pasado no es convertible, debe imprimir un mensaje de error
numero = input('Selecciona un numero: ')
print(f'Se ha seleccionado {numero} que es de forma {type(numero)} ')
def conv(a):
    if a.isdigit():
        a=int(a)
        print(f'Convertimos str a int: {type(a)}')
    else:
        print('Error')

conv(numero)


# EJERCICIO 2
# Crea una función llamada calcular_promedio que:
# Reciba una lista de números (enteros o flotantes).
# Calcule y devuelva el promedio (media aritmética) de los números en la lista.
# Si la lista está vacía, debe devolver None y mostrar un mensaje indicando que no hay datos para calcular. 

entrada = input("Introduce una lista de números (enteros o decimales) separados por comas: ")
def calcular_promedio(lista_numeros):
    promedio = sum(lista_numeros) / len(lista_numeros)
    return f"El promedio (media aritmética) es: {promedio}"
try:
    lista = [float(x) for x in entrada.split(',')]
    print(f"La lista es: {lista}")
    print(f"El tipo de la variable es: {type(lista)}")
    print(calcular_promedio(lista))
except:
    print("Error: todos los elementos deben ser números (enteros o decimales).")


# EJERCICIO 3
# Crea una función restar_numeros_pares(*args) que resten a la tabliable predefinida "total=50" 
# todos los números pares que se le pasen como argumentos posicionales.    

def restar_numeros_pares(*args): # args: tuplas
    total=50
    for num in args:
        if num % 2 ==0:
            total -= num
    return total

print(f'El resultado es {restar_numeros_pares(1,2,3,4)}')



# EJERCICIO 4
# Define una función imprimir_perfil(**kwargs) que reciba un diccionario y muestre la información como "clave: valor" para cada elemento.

def imprimir_perfil(**kwargs):
    texto = "" # definir la variable vacia
    for clave, valor in kwargs.items():
        texto += f"{clave}: {valor}\n" # \n sirve para hacer salto de linea
    return texto

dic = {
    "aisha": "22",
    "bea": "23"
}

print(imprimir_perfil(**dic))



# EJERCICIO 5
# Crea una función llamada mostrar_detalles que reciba:
# Cualquier cantidad de argumentos posicionales (*args), que representen características o detalles generales a mostrar.
# Cualquier cantidad de argumentos con nombre (**kwargs), que sean propiedades específicas asociadas a esas características con su valor.
# La función debe imprimir primero cada detalle general recibido (en el orden dado en args) y luego mostrar cada propiedad y su valor con formato clave = valor.
# Finalmente imprime el tipo de los args y los kwargs

def mostrar_detalles(*detalles1, **detalles2):

    for detalle in detalles1:
        print(f"Detalles del producto: {detalle}")

    for clave, valor in detalles2.items():
        print(f"Propiedades del producto: {clave} = {valor}")
        print(type(detalles1))
        print(type(detalles2))

# Ejemplo de uso
mostrar_detalles("Color rojo", "Bonito", "Talla M", peso=65, material='algodón')


# EJERCICIO 6
# Crea una función llamada venta_online que reciba los siguientes parámetros:

# pedido: un identificador del pedido (string).
# fecha_entrega: fecha estimada de entrega (string).
# incidencia: un parámetro opcional booleano que indica si hubo alguna incidencia con el pedido (por defecto es False).
# La función debe imprimir un mensaje diferente dependiendo del valor de incidencia:

# Si incidencia es True, imprimir "Contacte con Att. Cliente".
# Si incidencia es False, imprimir "Su pedido [pedido] se entregará el [fecha_entrega]".

def venta_online(pedido: str, fecha_entrega: str, incidencia: bool = False):
    text=""
    if incidencia == True:
        return f'Contacte con Att. Cliente'
    else:
        text += f"Su pedido {pedido} se entregará el {fecha_entrega}"
        return text 
    
print(venta_online("Pedido 1","13 enero", False))
    

# EJERCICIO 7
# Crea un programa donde se recojan dos inputs del usuario, y el output del programa sea si esos inputs son iguales o no

input1= input('Input 1: ')
input2= input('Input 2: ')

def input_iguales(input1,input2):
    if input1 == input2 :
        print ('Inputs iguales')
    else:
        print ('Inputs diferentes')
        
input_iguales(input1,input2)


# EJERCICIO 8
# Igual que el anterior, pero ahora tienen que ser tres inputs y dos salidas. 
# Una de las salidas que nos indique si todos son iguales, y la otra si al menos dos inputs sí que lo son

input1= input('Input 1: ')
input2= input('Input 2: ')
input3 = input('Input 3: ')

def comparacion(a, b, c):
    if a == b and b == c:
        print('Los tres inputs son iguales')
    elif a == b or a == c or b == c:
        print('Dos inputs son iguales')
    else:
        print('No se cumple ninguna condición')

comparacion(input1, input2, input3) # nota: hace distinccion entre mayusculas y minusculas ; este codigo es para texto


# EJERCICIO 9:
# Crea un programa que recoja dos inputs. Tiene que comprobar si su suma es igual, superior o inferior a 10.

inpu1 = float(input('Numero 1: '))
inpu2 = float(input('Numero 2: '))

def suma_comparacion(numero1,numero2):
    resultado_suma = numero1 + numero2
    if resultado_suma < 10:
        print(f'El resultado es menor de 10: {resultado_suma}')
    elif resultado_suma == 10:
        print(f'El resultado es igual de 10: {resultado_suma}')
    else:
        print(f'El resultado es igual de 10: {resultado_suma}')

suma_comparacion(inpu1,inpu2)


# EJERCICIO 10
# Haz una lista con números enteros.
# Inicializa una variable "total" en 0.
# Escribe un programa que calcule la suma acumulada hasta que el total exceda 100.
# Imprime cada valor que se suma y cuándo el total se pase de 100, imprime "Límite superado" y termina.

lista = [1, 15, 7, 8, 5, 80, 0, 11, 4, 13]
total = 0 
for num in lista:
    total += num
    print(f"Sumando {num}, total = {total}")
    if total > 100:
        print("Límite superado")
        break



# EJERCICIO 11
# Tienes la siguiente lista:
# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# Implementa un programa que recorra cada elemento e imprima por pantalla todos los que sean divisibles por 5. 
# Si nos encontramos con alguno que sea mayor que 150, detener el bucle.

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for num in list1:
    if num > 150: # MUY IMPORTANTE: debemos de poner primero la condición que requiere el break !!!!!
        print(f'Detenemos bucle porque {num} es mayor que 150')
        break
    if num % 5 == 0:
        print(f'{num} es divisible por 5')



# EJERCICIO 12
# Crea un programa que:
# Pida al usuario ingresar un precio con decimales (por ejemplo, 12.98765).
# Pida al usuario cuántos decimales quiere mostrar (un número entero).
# Use la función round() para redondear el precio al número de decimales indicados.
# Imprima el precio redondeado con el formato: "El precio redondeado es: [precio]"

precio = float(input('Introduce un numero con decimales: '))
mostrar_decimales = int(input('Indica el numero de decimales que quiere mostrar: '))

def redondeo(precio,mostrar_decimales):
    print(f'El precio redondeado es {round(precio,mostrar_decimales)}')

redondeo(precio,mostrar_decimales)