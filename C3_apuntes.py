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
lista_edades=[15, 22, 17, 30, 65, 45, 70, 19]

for edad in lista_edades:
    if edad > 18 and edad < 65:
        print(f"Edad {edad} es mayor de edad.")
    elif edad >= 65:
        print(f"Ejecución detenida por edad avanzada.")
        break


