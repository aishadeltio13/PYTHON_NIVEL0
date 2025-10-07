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




        
    

