unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

def numero_a_texto(numero):
    if numero < 0 or numero > 1000000:
        return "Número fuera de rango"
    
    if numero < 10:
        return unidades[numero]
    
    elif numero < 100:
        decena = numero // 10
        unidad = numero % 10
        if unidad == 0:
            return decenas[decena]
        else:
            return decenas[decena] + " y " + unidades[unidad]
    
    elif numero == 100:
        return "cien"
    
    elif numero < 1000:
        centena = numero // 100
        resto = numero % 100
        if resto == 0:
            return centenas[centena]
        else:
            return centenas[centena] + " " + numero_a_texto(resto)
    
    elif numero < 10000:
        mil = numero // 1000
        resto = numero % 1000
        if resto == 0:
            return "mil"
        elif mil == 1:
            return "mil " + numero_a_texto(resto)
        else:
            return numero_a_texto(mil) + " mil " + numero_a_texto(resto)
    
    elif numero < 1000000:
        miles = numero // 1000
        resto = numero % 1000
        if resto == 0:
            return numero_a_texto(miles) + " mil"
        else:
            return numero_a_texto(miles) + " mil " + numero_a_texto(resto)
            
# Ejecución del codigo
try:
    numero = int(input("Ingrese un número entre 0 y 1,000,000: "))
    resultado = numero_a_texto(numero)
    print(f"El número {numero} en texto es: {resultado}")
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número válido.")
