def formatNumber(numero):
    # Paso 1: Convertir el número entero a una cadena de texto
    numero_str = str(numero)
    
    # Paso 2: Invertir la cadena
    numero_invertido = numero_str[::-1]
    
    # Paso 3: Agregar puntos cada tres caracteres desde el inicio
    resultado = ""
    for i in range(len(numero_invertido)):
        if i % 3 == 0 and i!= 0:
            resultado += "."
        resultado += numero_invertido[i]
    
    # Paso 4: Invertir nuevamente para obtener el formato deseado
    return resultado[::-1]