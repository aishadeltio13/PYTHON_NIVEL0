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
# Crea una función restar_numeros_pares(*args) que resten a la tabliable predefinida "total=50" todos los números pares que se le pasen como argumentos posicionales.    
