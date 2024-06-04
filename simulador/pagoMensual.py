def pagoMensual(monto, tasa, cuotas):
    currentMonto = int(monto.replace(".", ""))
    tasaMensual = round(tasa / 12, 2)
    tasaMes = tasaMensual / 100
    tasaElevada = (tasaMes + 1) ** int(cuotas)
    numerador = int(currentMonto) * tasaMes * tasaElevada
    denominador = tasaElevada - 1
    total = int(numerador / denominador)
    return total