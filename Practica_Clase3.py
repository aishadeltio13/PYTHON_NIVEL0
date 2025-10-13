# EJERCICIO 1
# Crea una función que convierta un str en un número. Si el argumento pasado no es convertible, debe imprimir un mensaje de error
# numero = input('Selecciona un numero: ')
# print(f'Se ha seleccionado {numero} que es de forma {type(numero)} ')

# def conv(a):
#     if a.isdigit():
#         a=int(a)
#         print(f'Convertimos str a int: {type(a)}')
#     else:
#         print('Error')

# conv(numero)


# EJERCICIO 2
# Crea una función llamada calcular_promedio que:
# Reciba una lista de números (enteros o flotantes).
# Calcule y devuelva el promedio (media aritmética) de los números en la lista.
# Si la lista está vacía, debe devolver None y mostrar un mensaje indicando que no hay datos para calcular. 

# entrada = input("Introduce una lista de números (enteros o decimales) separados por comas: ")
# def calcular_promedio(lista_numeros):
#     promedio = sum(lista_numeros) / len(lista_numeros)
#     return f"El promedio (media aritmética) es: {promedio}"
# try:
#     lista = [float(x) for x in entrada.split(',')]
#     print(f"La lista es: {lista}")
#     print(f"El tipo de la variable es: {type(lista)}")
#     print(calcular_promedio(lista))
# except:
#     print("Error: todos los elementos deben ser números (enteros o decimales).")


# EJERCICIO 3
# Crea una función restar_numeros_pares(*args) que resten a la tabliable predefinida "total=50" 
# todos los números pares que se le pasen como argumentos posicionales.    

# def restar_numeros_pares(*args): # args: tuplas
#     total=50
#     for num in args:
#         if num % 2 ==0:
#             total -= num
#     return total

# print(f'El resultado es {restar_numeros_pares(1,2,3,4)}')



# EJERCICIO 4
# Define una función imprimir_perfil(**kwargs) que reciba un diccionario y muestre la información como "clave: valor" para cada elemento.

# def imprimir_perfil(**kwargs):
#     texto = "" # definir la variable vacia
#     for clave, valor in kwargs.items():
#         texto += f"{clave}: {valor}\n" # \n sirve para hacer salto de linea
#     return texto

# dic = {
#     "aisha": "22",
#     "bea": "23"
# }

# print(imprimir_perfil(**dic))



# EJERCICIO 5
# Crea una función llamada mostrar_detalles que reciba:

# Cualquier cantidad de argumentos posicionales (*args), que representen características o detalles generales a mostrar.
# Cualquier cantidad de argumentos con nombre (**kwargs), que sean propiedades específicas asociadas a esas características con su valor.
# La función debe imprimir primero cada detalle general recibido (en el orden dado en args) y luego mostrar cada propiedad y su valor con formato clave = valor.

# Finalmente imprime el tipo de los args y los kwargs

# def mostrar_detalles(*detalles1, **detalles2):

#     for detalle in detalles1:
#         print(f"Detalles del producto: {detalle}")

#     for clave, valor in detalles2.items():
#         print(f"Propiedades del producto: {clave} = {valor}")
#         print(type(detalles1))
#         print(type(detalles2))

# # Ejemplo de uso
# mostrar_detalles("Color rojo", "Bonito", "Talla M", peso=65, material='algodón')


# EJERCICIO 6
# Crea una función llamada venta_online que reciba los siguientes parámetros:

# pedido: un identificador del pedido (string).
# fecha_entrega: fecha estimada de entrega (string).
# incidencia: un parámetro opcional booleano que indica si hubo alguna incidencia con el pedido (por defecto es False).
# La función debe imprimir un mensaje diferente dependiendo del valor de incidencia:

# Si incidencia es True, imprimir "Contacte con Att. Cliente".
# Si incidencia es False, imprimir "Su pedido [pedido] se entregará el [fecha_entrega]".

# def venta_online(pedido: str, fecha_entrega: str, incidencia: bool = False):
#     text=""
#     if incidencia == True:
#         return f'Contacte con Att. Cliente'
#     else:
#         text += f"Su pedido {pedido} se entregará el {fecha_entrega}"
#         return text 
    
# print(venta_online("Pedido 1","13 enero", False))
    

# EJERCICIO 7
# Crea un programa donde se recojan dos inputs del usuario, y el output del programa sea si esos inputs son iguales o no
