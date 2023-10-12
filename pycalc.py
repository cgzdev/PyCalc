# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Solicitar al usuario que elija una operación (suma o resta)
operacion = input("Elija una operación (suma o resta): ")

if operacion.lower() == "suma":
    resultado = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es: {resultado}")
elif operacion.lower() == "resta":
    resultado = numero1 - numero2
    print(f"La resta de {numero1} y {numero2} es: {resultado}")
else:
    print("Operación no válida. Por favor, elija 'suma' o 'resta'.")
