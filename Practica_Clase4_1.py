# EJERCICIO 1
# Crea una clase CuentaBancaria con:
# Atributos: titular (str) y saldo (float).
# Método depositar(cantidad) que sume al saldo (no permite montos ≤ 0).
# Método mostrar() que devuelva un string del estilo: "Titular: Ana | Saldo: 125.50€".

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self,cantidad):
        if cantidad <=0:
            print('No se está aumentando el saldo')
        elif cantidad > 0:
            self.saldo += cantidad
            print(f'Se ha aumentado el saldo: {self.saldo}')
            
    def mostrar(self):
        print(f'Titular: {self.titular} | Saldo: {self.saldo}')
        
persona1 = CuentaBancaria("Ana", 1.200)
persona1.mostrar()
persona1.depositar(10)
persona1.mostrar()


# EJERCICIO 2
# Crea un programa que divida dos números introducidos por el usuario. 
# Utiliza try y except para manejar posibles errores de división por cero. Si se produce un error, 
# imprime "No se puede dividir por cero". Si no, imprime el resultado.

numero1 = float(input('Número 1: '))
numero2 = float(input('Número 2: '))

lista_numeros = [numero1, numero2] 

try:
    for x in lista_numeros:
        if x % 0 == 0:
            print(f'{x} es divisble por cero')
except:
    print('Error')
    
    
    

    