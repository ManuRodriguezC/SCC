def controls(datas):
    activos = int(datas['salario'].replace(".", "")) + int(datas['others'].replace(".", ""))
    print(f"Activos - {activos}")
    pasivos = int(datas['debit'].replace(".", ""))
    print(f"Pasivos - {pasivos}")
    total = activos - pasivos
    print(f"Total - {total}")
    
    print(datas['creditType'].plazoMax)
    
    if int(datas['cuotas']) > int(datas['creditType'].plazoMax):
        return {'error': True, 'mensaje': f"El plazo maximo de cuotas es de {datas['creditType'].plazoMax}."}
    
    return "Check"