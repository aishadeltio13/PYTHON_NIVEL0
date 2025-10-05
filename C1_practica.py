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
a = gente[3]
if a["edad"] >= 18:
    print("1) mayor")
else:
    print("1) menor")

# Ejercicio 2:
b = gente[1]["nombre"]
if b[0] == "J":
    print("Empieza por J")
else:
    print("No empieza por J")

# Ejercicio 3:
c = gente[3]["nombre"]

if len(c) == 4:
    print("4 letras")
else:
    print("Otra longitud")
    
# Ejercicio 4:
p = gente[4]
if p["edad"] % 2 == 0:
    print("par")
else:
    print("impar")
    
# Ejercicio 5:
p = gente[0]
if p["nombre"].endswith("o"):
    print("Termina en o")
else:
    print("No termina en o")


# # NIVEL 2 # #

# Ejercicio 1:
a = gente[1]
if a["nombre"].startswith("J") and a["edad"] < 40:
    print("6) J y <40")
else:
    print("6) no cumple")

# Ejercicio 2:
b = gente[5]["nombre"]

if "a" in b or "A" in b:
    print("Contiene A")
else:
    print("No contiene A")

# Ejercicio 3:
c = gente[4]["edad"]
if c > 20 and c < 35:
    print("Entre 20 y 35")
else:
    print("No está entre 20 y 35")
    
# Ejercicio 4:
d1 = gente[2]["nombre"]
d2 = gente[2]["edad"]

if "J" in b or "j" in d1 and d2 < 30:
    print("J y <30")
else:
    print("No cumple")
    
# Ejercicio 5:
e1 = gente[1]["nombre"]
e2 = gente[0]["edad"]
if "J" in e1 or "j" in e1 or e2 < 25:
    print("o 'J' o <30")
else:
    print("No cumple")



# # NIVEL 3 # #

# Ejercicio 1:
a = gente[1]
b = gente[2]

if a["edad"] > b["edad"]:
    print(f"{a['nombre']} es mayor que {b['nombre']}")
elif a["edad"] < b["edad"]:
    print(f"{b['nombre']} es mayor que {a['nombre']}")  
else:
    print(f"{a['nombre']} y {b['nombre']} tienen la misma edad")

# Ejercicio 2:
a= gente[5]["nombre"]
b = gente[4]["nombre"]

if len(a) > len(b):
    print(f"{a} tiene un nombre más largo que {b}") 
elif len(a) < len(b):
    print(f"{b} tiene un nombre más largo que {a}")
else:
    print(f"{a} y {b} tienen misma longitud sus nombre")

# Ejercicio 3:
a = gente[0]  # Jamiro 45
b = gente[1]  # Juan   35
c = gente[2]  # Paco   34
if a["edad"] >= b["edad"] and a["edad"] >= c["edad"]:
    print(f"16) mayor: {a['nombre']}")
elif b["edad"] >= a["edad"] and b["edad"] >= c["edad"]:
    print(f"16) mayor: {b['nombre']}")
else:
    print(f"16) mayor: {c['nombre']}")

    
 





