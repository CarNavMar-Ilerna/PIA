#Ejercicios clases y objetos

#Clase Cuenta Bancaria
class CuentaBancaria:
    def __init__(self, titular, saldo, tipodecuenta):
        self.titular = titular
        self.saldo = saldo
        self.tipodecuenta = tipodecuenta
        pass
    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Depósito exitoso. Nuevo saldo: {self.saldo}."
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return "Fondos insuficientes."
        else:
            self.saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: {self.saldo}."
    def mostrar_saldo(self):
        return f"El saldo actual es: {self.saldo}."
    
cuenta1 = CuentaBancaria("Carlos", 1000, "Ahorros")
cuenta2 = CuentaBancaria("María", 500, "Corriente")

print(cuenta1.mostrar_saldo())
print(cuenta1.depositar(200))
print(cuenta1.retirar(1500))
print(cuenta1.retirar(300))
print(cuenta1.mostrar_saldo())
print(cuenta2.mostrar_saldo())
print(cuenta2.depositar(100))
print(cuenta2.retirar(700))
print(cuenta2.retirar(200))
print(cuenta2.mostrar_saldo())