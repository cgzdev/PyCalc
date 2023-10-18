unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]
decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
miles_de_millar = ["", "mil", "millón", "mil millones"]

# Definimos el rango del código llegando hasta 1,000,000,000,000
def numero_a_texto(numero):
    if numero < 0 or numero > 1000000000000: # Mensaje si el número está fuera del rango
        return "Número fuera de rango"
    if numero == 0:                          # Mensaje si el número es Cero
        return "cero"

    if numero < 20:                          # Números menores al 20
        return unidades[numero]
        
    if numero == 20:                         # Número 20
        return "veinte"

    if numero == 21:                         # Número 21
        return "veintiuno"
        
    elif numero >= 22 and numero < 30:       # Resto de números entre 22 y 30
        unidad = numero % 10
        return "veinti" + unidades[unidad]

    elif numero < 100:                       # Resto de número menores que 100
        decena = numero // 10
        unidad = numero % 10
        if unidad == 0:
            return decenas[decena]
        else:
            return decenas[decena] + " y " + unidades[unidad]
        
    elif numero == 100:                      # Número 100
        return "cien"

    elif numero < 1000:                      # Números menores a 1000
        centena = numero // 100
        resto = numero % 100
        if centena == 1 and resto == 0:
            return "cien"
        else:
            return centenas[centena] + " " + numero_a_texto(resto)

    elif numero < 10000:                     # Números menores a 10000
        mil = numero // 1000
        resto = numero % 1000
        if resto == 0:
            return "mil"
        elif mil == 1:
            return "mil " + numero_a_texto(resto)
        else:
            return numero_a_texto(mil) + " mil " + numero_a_texto(resto)
        
    elif numero == 21000:                    # Caso especial 21000
            return "veintiún" + " " + "mil"

    elif numero < 1000000:                   # Números menores a 1,000,000 (un millón)
        mil = numero // 1000
        resto = numero % 1000
        if resto == 0:
            return numero_a_texto(mil) + " mil"
        else:
            return numero_a_texto(mil) + " mil " + numero_a_texto(resto)

    elif numero == 1000000:                  # Número 1,000,000 (un millón)
        return "un millón"

    elif numero < 1000000000:                # Números menores a 1,000,000,000 (mil millones)
        millones = numero // 1000000
        resto = numero % 1000000
        if resto == 0:
            return numero_a_texto(millones) + " millones"
        else:
            return numero_a_texto(millones) + " millones " + numero_a_texto(resto)

    elif numero == 1000000000:               # Número 1,000,000,000 (mil millones)
        return "un mil millones"

    elif numero < 1000000000000:             # Números menores a 1,000,000,000,000 (un billón)
        billones = numero // 1000000000
        resto = numero % 1000000000
        if resto == 0:
            return numero_a_texto(billones) + " mil millones"
        else:
            return numero_a_texto(billones) + " mil millones " + numero_a_texto(resto)

    elif numero == 1000000000000:            # Número 1,000,000,000,000 (un billón)
        return "un billón"

# Ejecución del código
try:
    numero = int(input("Ingrese un número entre 0 y 1,000,000,000,000 (un billón): "))
    print(numero_a_texto(numero))
except ValueError:
    print("Por favor, ingrese un número válido.")