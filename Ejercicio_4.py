# Definimos la clase CuentaBancaria
class CuentaBancaria:
    """Clase que representa una cuenta bancaria con número de cuenta y saldo."""

    def __init__(self, numero_cuenta, saldo=100000):
        """Constructor que inicializa el número de cuenta con saldo inicial de 100,000 COP."""
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        """Método para depositar dinero en la cuenta."""
        self.saldo += cantidad
        print(f"Depósito exitoso: ${cantidad} COP. Saldo actual: ${self.saldo} COP")

    def retirar(self, cantidad):
        """Método para retirar dinero de la cuenta, verificando si hay fondos suficientes."""
        if cantidad > self.saldo:
            print(f"Fondos insuficientes. Saldo disponible: ${self.saldo} COP")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso: ${cantidad} COP. Saldo actual: ${self.saldo} COP")

# Creación de una instancia de CuentaBancaria con saldo inicial de 100,000 COP
cuenta = CuentaBancaria(numero_cuenta="213023_198")

# Menú para que el usuario elija entre depositar o retirar
print("\nSeleccione una opción:")
print("1. Depositar dinero")
print("2. Retirar dinero")

opcion = input("Ingrese el número de la opción: ").strip()

# Se ejecuta la acción según la elección del usuario
if opcion == "1":
    cantidad = int(input("Ingrese la cantidad a depositar: "))
    cuenta.depositar(cantidad)
elif opcion == "2":
    cantidad = int(input("Ingrese la cantidad a retirar: "))
    cuenta.retirar(cantidad)
else:
    print("Opción no válida. Debes elegir 1 o 2.")

# Mostrar el saldo final
print(f"Saldo final en la cuenta {cuenta.numero_cuenta}: ${cuenta.saldo} COP")
