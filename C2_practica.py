gente = [
    {"nombre": "Jamiro", "edad": 45},
    {"nombre": "Juan",   "edad": 35},
    {"nombre": "Paco",   "edad": 34},
    {"nombre": "Pepe",   "edad": 14},
    {"nombre": "Pilar",  "edad": 24},
    {"nombre": "Laura",  "edad": 24},
    {"nombre": "Jenny",  "edad": 10},
]

# # NIVEL 1 # #

# Ejercicio 1:
for persona in gente:
    if len(persona["nombre"]) == 4:
        print(persona["nombre"]) # No poner print en los bucles.
        
# Otra forma:
nombres_4_letras = []  # Lista vacía
for persona in gente:
    if len(persona["nombre"]) == 4:
        nombres_4_letras.append(persona)

print("Nombres con 4 letras:", nombres_4_letras)

# Ejercicio 2:
nombres_J_menor40 = []  # Lista vacía

for persona in gente:
    if persona["nombre"][0].lower()=="j" and persona["edad"] < 40: # alternativa: persona["nombre"].startswith("J")
        nombres_J_menor40.append(persona)
        
print("Nombres que empiezan por J y son menores de 40:", nombres_J_menor40)


# # NIVEL 2 # #

# Ejercicio 1:
def resta(a,b):
    return a - b

a= 5
b= 3
resta(a,b)
print(f"La resta entre {a} y {b} es: {resta(a,b)}")

# Ejercicio 2:

def DuplicaNumero(a):
    if type(a)== float or type(a)== int:
        return a*2
    else:
        return "El valor debe ser numérico"
a= 5
print(f"El doble de {a} es: {DuplicaNumero(a)}")
b= "hola"
print(f"El doble de {b} es: {DuplicaNumero(b)}")

# Ejercicio 3:
def ultimoCaracter(a):
    if type(a) == str and a != "":
        return a[-1]
    elif a == "":
        return "El valor debe ser una cadena de texto no vacía"
    else:
        return "El valor debe ser una cadena"
    
a1= "aisha"
a2= ""
a3= 7
print(f"El último caracter de {a1} es: {ultimoCaracter(a1)}")
print(f"El último caracter de una cadena vacía es: {ultimoCaracter(a2)}")
print(f"El último caracter de {a3} es: {ultimoCaracter(a3)}")

# Alternativa ejercicio 3:
def ultimoCaracter(cadena):
    """
    Devuelve el último carácter de un string.
    Valida si es string y no está vacío.
    """
    if not isinstance(cadena, str): # isinstance: comprueba el tipo de dato
        return "Debo ser ejecutada con un string"
    if cadena == "":
        return "Debo ser ejecutada con un string no vacío"
    return cadena[-1]

# Ejercico 4:
def cuentaCaracteres(c):
    if type(c) == str:
        x = len(c)
        return f'La palabra {c} tiene {x} caracteres'
    else:
        return "Debo ser ejecutada con un string"

a1= "Hola Mundo"
a2= 7
print(cuentaCaracteres(a1)) # 10
print(cuentaCaracteres(a2)) # Error


 




        
    

