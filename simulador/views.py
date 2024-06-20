from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SalaryForm, SocialesRetencionForm, SocialesForm, ExtraForm, TasasForm
from .models import Salary, SocialesRetencion, Sociales, Extra, Tasas
from django.contrib import messages
from .pagoMensual import pagoMensual
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import datetime
from .formatNumber import formatNumber


def simulador(request):
    socialesRetencion = SocialesRetencion.objects.all()
    sociales = Sociales.objects.all()
    extras = Extra.objects.all()
    
    salario = Salary.objects.all()
    currentSalari = salario[0].value.replace(".", "")

    if request.method == 'POST':
        data = {
            'name' : request.POST.get('name'),
            'lastname': request.POST.get('lastname'),
            'document': request.POST.get('document'),
            'salario': request.POST.get('salario'),
            'others': request.POST.get('others'),
            'debit': request.POST.get('debit'),
        }
        
        valuesTypecredit = ['typecredit1', 'typecredit2', 'typecredit3']
        typeCredit = next((request.POST.get(value) for value in valuesTypecredit if request.POST.get(value)))
        
        valuesMonto = ['monto1', 'monto2', 'monto3']
        monto = next((request.POST.get(value) for value in valuesMonto if request.POST.get(value)))
        
        valuesCuotas = ['cuotas1', 'cuotas2', 'cuotas3']
        cuotas = next((request.POST.get(value) for value in valuesCuotas if request.POST.get(value)))
        
        tipocredito = ""
    
        if SocialesRetencion.objects.filter(name=typeCredit).exists():
            tipocredito = "socialretencion"
            currentType = SocialesRetencion.objects.get(name=typeCredit)
            plazoMax = currentType.plazoMax
            aportes = request.POST.get('aportes')
            montoMaximoCredit = int(int(aportes.replace(".", "")) * float(currentType.aportesMax / 100))
            rangos1 = currentType.rango1.split(" ")
            rangos2 = currentType.rango2.split(" ")
            rangos3 = currentType.rango3.split(" ")
            rangos4 = currentType.rango4.split(" ")
            rangos5 = currentType.rango5.split(" ")
            rangos6 = currentType.rango6.split(" ")
            rangos7 = currentType.rango7.split(" ")
            if int(cuotas) >= int(rangos1[1]) and int(cuotas) <= int(rangos1[3]):
                tasa = float(rangos1[5])
            if int(cuotas) >= int(rangos2[1]) and int(cuotas) <= int(rangos2[3]):
                tasa = float(rangos2[5])
            if int(cuotas) >= int(rangos3[1]) and int(cuotas) <= int(rangos3[3]):
                tasa = float(rangos3[5])
            if int(cuotas) >= int(rangos4[1]) and int(cuotas) <= int(rangos4[3]):
                tasa = float(rangos4[5])
            if int(cuotas) >= int(rangos5[1]) and int(cuotas) <= int(rangos5[3]):
                tasa = float(rangos5[5])
            if int(cuotas) >= int(rangos6[1]) and int(cuotas) <= int(rangos6[3]):
                tasa = float(rangos6[5])
            if int(cuotas) >= int(rangos7[1]) and int(cuotas) <= int(rangos7[3]):
                tasa = float(rangos7[5])
        elif Sociales.objects.filter(name=typeCredit).exists():
            currentType = Sociales.objects.get(name=typeCredit)
            plazoMax = currentType.plazoMax
            rangos1 = currentType.rango1.split(" ")
            if int(cuotas) >= int(rangos1[1]) and int(cuotas) <= int(rangos1[3]):
                tasa = float(rangos1[5])
            rangos2 = currentType.rango2.split(" ")
            if int(cuotas) >= int(rangos2[1]) and int(cuotas) <= int(rangos2[3]):
                tasa = float(rangos2[5])
            rangos3 = currentType.rango3.split(" ")
            if int(cuotas) >= int(rangos3[1]) and int(cuotas) <= int(rangos3[3]):
                tasa = float(rangos3[5])
            rangos4 = currentType.rango4.split(" ")
            if int(cuotas) >= int(rangos4[1]) and int(cuotas) <= int(rangos4[3]):
                tasa = float(rangos4[5])
            if currentType.rango5:
                rangos5 = currentType.rango5.split(" ")
                if int(cuotas) >= int(rangos5[1]) and int(cuotas) <= int(rangos5[3]):
                    tasa = float(rangos5[5])
            if currentType.rango6:
                rangos6 = currentType.rango6.split(" ")
                if int(cuotas) >= int(rangos6[1]) and int(cuotas) <= int(rangos6[3]):
                    tasa = float(rangos6[5])
            if currentType.rango7:
                rangos7 = currentType.rango7.split(" ")
                if int(cuotas) >= int(rangos7[1]) and int(cuotas) <= int(rangos7[3]):
                    tasa = float(rangos7[5])
            if currentType.rango8:
                rangos8 = currentType.rango8.split(" ")
                if int(cuotas) >= int(rangos8[1]) and int(cuotas) <= int(rangos8[3]):
                    tasa = float(rangos8[5]) 
        else:  
            if Extra.objects.filter(name=typeCredit).exists():
                currentType = Extra.objects.get(name=typeCredit)
                if int(cuotas) > int(currentType.plazoMax):
                    messages.error(request, f"El plazo máximo de cuotas para la linea {currentType.name} es {currentType.plazoMax}.")
                    return redirect('/')
                typeperson = request.POST.get('typeperson')
                tasas = Tasas.objects.filter(name=typeperson)
                score = request.POST.get('score')
                if int(score) > 1000 or int(score) <= 0:
                    messages.error(request, f"El rango de score debe estar entre 1 y 1000")
                    return redirect('/')
                for tasa in tasas:
                    if int(score) > float(tasa.scoreMin) and int(score) <= float(tasa.scoreMax):
                        plazoMax = tasa.plazoMax
                        tasa = float(tasa.tasa)
                        break
                    else:
                        messages.error(request, f"Su score no aplica para solicitar un credito.")
                        return redirect('/')
                        

        request.session['form_data'] = data
        
        # montoMaximoCredit = int(currentSalari.replace(".", "")) * currentType.montoMax
        print(plazoMax)
        if int(cuotas) > int(plazoMax):
            messages.error(request, f"El plazo máximo de cuotas es {plazoMax}.")
            return redirect('/')
        
        ingresosSalario = int(data['salario'].replace(".", ""))
        seguridadSocial = (ingresosSalario * 8) / 100
        ingresosOtros = int(data['others'].replace(".", ""))
        egresos = int(data['debit'].replace(".", ""))
        ingresosTotales = ingresosSalario + ingresosOtros
        
        capacidadPago = int(((ingresosTotales * 30) / 100) - egresos)
        montoMensual = pagoMensual(monto, tasa, cuotas)
        
        montoMax = int((int(monto.replace(".", "")) * capacidadPago) / montoMensual)

        if tipocredito == "socialretencion":
            montoMax = montoMaximoCredit

        if tipocredito != "socialretencion":
            if int(monto.replace(".", "")) > montoMax:
                if montoMax < 0:
                    messages.error(request, f"Su capacidad de pago no aplica para solicitar un crédito.")
                else:
                    number = formatNumber(montoMax)
                    messages.error(request, f"El monto máximo según la capacidad de pago es de $ {number}")
                return redirect('/')
        else:
            if int(monto.replace(".", "")) > montoMaximoCredit:
                number = formatNumber(montoMaximoCredit)
                messages.error(request, f"El monto máximo a solicitar es de $ {number}")
                return redirect('/')
        
        datas = {
            'data': data,
            'type': currentType.name,
            'monto': monto,
            'cuotas': cuotas,
            'tasaAnual': round(tasa * 12, 4),
            'tasaMensual': tasa,
            'garantias': currentType.garantia,
            'requisitos': currentType.requisitos,
            'seguridad': int(seguridadSocial),
            'totales': int(ingresosTotales),
            'cuota': montoMensual,
            'capacidad': capacidadPago,
            'montomaximo': montoMax
        }
        del request.session['form_data']
        request.session['calculos'] = {'datas': datas}
        return redirect('simulacion')

    form_data = request.session.get('form_data', {})
    return render(request, 'simulador.html', {
        'socialesRetencion': socialesRetencion,
        'sociales': sociales,
        'extras': extras,
        'form_data': form_data
    })
    
def simulacion(request):
    datos = request.session.get('calculos', {})
    return render(request, 'dialog.html', datos)

@login_required
def socialRetencion(request):
    socialreten = SocialesRetencion.objects.all()
    if request.method == 'POST':
        form = SocialesRetencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/socialesretencion')
    else:
        form = SocialesRetencionForm()
    return render(request, 'socialesretencion/socialretencion.html',
                  {'socialreten': socialreten,
                   'form': form})

@login_required
def update_socialRetencion(request, id):
    socialesReten = get_object_or_404(SocialesRetencion, id=id)

    if request.method == 'POST':
        form = SocialesRetencionForm(request.POST, instance=socialesReten)
        if form.is_valid():
            form.save()
            return redirect('/socialesretencion')
    else:
        form = SocialesRetencionForm(instance=socialesReten)

    return render(request, 'socialesretencion/updatesocialesretencion.html', {'form': form})

@login_required
def delete_socialRetencion(request, id):
    """"""
    socialesreten = get_object_or_404(SocialesRetencionForm, id=id)
    socialesreten.delete()
    return redirect('/socialesreten')


@login_required
def social(request):
    social = Sociales.objects.all()
    if request.method == 'POST':
        form = SocialesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sociales')
    else:
        form = SocialesForm()
    return render(request, 'sociales/sociales.html',
                  {'social': social,
                   'form': form})

@login_required
def update_social(request, id):
    sociales = get_object_or_404(Sociales, id=id)

    if request.method == 'POST':
        form = SocialesForm(request.POST, instance=sociales)
        if form.is_valid():
            form.save()
            return redirect('/sociales')
    else:
        form = SocialesForm(instance=sociales)

    return render(request, 'sociales/updatesociales.html', {'form': form})

@login_required
def delete_social(request, id):
    """"""
    socialesreten = get_object_or_404(SocialesForm, id=id)
    socialesreten.delete()
    return redirect('/sociales')


@login_required
def extra(request):
    extras = Extra.objects.all()
    if request.method == 'POST':
        form = ExtraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/extras')
    else:
        form = ExtraForm()
    return render(request, 'extras/extras.html',
                  {'extras': extras,
                   'form': form})

@login_required
def update_extra(request, id):
    extra = get_object_or_404(Extra, id=id)

    if request.method == 'POST':
        form = ExtraForm(request.POST, instance=extra)
        if form.is_valid():
            form.save()
            return redirect('/extras')
    else:
        form = ExtraForm(instance=extra)
    return render(request, 'extras/updateextra.html', {'form': form})

@login_required
def delete_extra(request, id):
    """"""
    extra = get_object_or_404(Extra, id=id)
    extra.delete()
    return redirect('/extras')


@login_required
def tasas(request):
    tasas = Tasas.objects.all()
    if request.method == 'POST':
        form = TasasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasas')
    else:
        form = TasasForm()
    return render(request, 'tasas/tasas.html',
                  {'tasas': tasas,
                   'form': form})

@login_required
def update_tasa(request, id):
    tasa = get_object_or_404(Tasas, id=id)

    if request.method == 'POST':
        form = TasasForm(request.POST, instance=tasa)
        if form.is_valid():
            form.save()
            return redirect('/tasas')
    else:
        form = TasasForm(instance=tasa)
    return render(request, 'tasas/updatetasa.html', {'form': form})

@login_required
def delete_tasa(request, id):
    """"""
    tasa = get_object_or_404(Tasas, id=id)
    tasa.delete()
    return redirect('/tasas')


@login_required
def salary(request):
    currentSalary = Salary.objects.all()
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/salario')
    else:
        form = SalaryForm()
    return render (request, 'salario/salario.html',
                   {'salarios': currentSalary,
                    'form': form})

@login_required
def updateSalary(request, id):
    salario = get_object_or_404(Salary, id=id)
    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=salario)
        if form.is_valid():
            form.save()
            return redirect('/salario')
    else:
        form = SalaryForm(instance=salario)
    return render(request, 'salario/updatesalario.html', {'form': form})

@login_required
def delete_salario(request, id):
    salario = get_object_or_404(Salary, id=id)
    salario.delete()
    return redirect('/salario')

def generatePdf(request):
    """"""
    datos = request.session.get('calculos', {})
    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    
    # p.drawImage("http://127.0.0.1:6001/static/images/logo_cootratiempo.jpg", 30, 730, width=60, height=80)
    p.setFont("Helvetica-Bold", 25)
    p.setFillColorRGB(0.196, 0.333, 0.627)
    p.drawString(110, 760, "Simulación de Credito Cootratiempo")
        
    p.roundRect(360, 700, width=150, height=30, radius=10)
    p.setFont("Helvetica-Bold", 10)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(380, 718, "Fecha:")
    p.drawString(380, 705, str(datetime.datetime.now()).split(".")[0])
    
    p.setFont("Helvetica-Bold", 18)
    p.setFillColorRGB(0.196, 0.333, 0.627)
    p.drawString(200, 670, "Información Asociado")
    
    p.roundRect(90, 555, width=420, height=105, radius=10)
    p.setFont("Helvetica", 12)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(125, 640, "Nombre Asociado")
    p.drawString(350, 640, datos['datas']['data']['name'])
    p.drawString(125, 625, "Apellido Asociado")
    p.drawString(350, 625, datos['datas']['data']['lastname'])
    p.drawString(125, 610, "Documento Asociado")
    p.drawString(350, 610, datos['datas']['data']['document'])
    p.drawString(125, 595, "Salario")
    p.drawString(350, 595, f"$ {datos['datas']['data']['salario']}")
    p.drawString(125, 580, "Otros Ingresos")
    p.drawString(350, 580, f"$ {datos['datas']['data']['others']}")
    p.drawString(125, 565, "Debitos")
    p.drawString(350, 565, f"$ {datos['datas']['data']['debit']}")

    p.setFont("Helvetica-Bold", 18)
    p.setFillColorRGB(0.196, 0.333, 0.627)
    p.drawString(200, 520, "Datos de la Solicitud")
    
    p.setFont("Helvetica", 12)
    p.setFillColorRGB(0, 0, 0)
    p.roundRect(90, 420, width=420, height=90, radius=10)
    p.drawString(125, 490, "Tipo de Credito")
    p.drawString(350, 490, str(datos['datas']['type']))
    p.drawString(125, 475, "Monto a Solicitar")
    p.drawString(350, 475, f"$ {str(datos['datas']['monto'])}")
    p.drawString(125, 460, "Numero de cuotas")
    p.drawString(350, 460, str(datos['datas']['cuotas']))
    p.drawString(125, 445, "Tasa Nominal Anual")
    p.drawString(350, 445, f"{str(datos['datas']['tasaAnual'])} %")
    p.drawString(125, 430, "Tasa Nominal Mensual")
    p.drawString(350, 430, f"{str(datos['datas']['tasaMensual'])} %")
    
    
    p.setFont("Helvetica-Bold", 18)
    p.setFillColorRGB(0.196, 0.333, 0.627)
    p.drawString(180, 385, "Datos de la Simulación")
    
    p.setFont("Helvetica", 12)
    p.setFillColorRGB(0, 0, 0)
    p.roundRect(90, 285, width=420, height=90, radius=10)
    p.drawString(125, 355, "Aporte seguridad social")
    p.drawString(350, 355, f"$ {formatNumber(str(datos['datas']['seguridad']))}")
    p.drawString(125, 340, "Ingresos Totales")
    p.drawString(350, 340, f"$ {formatNumber(str(datos['datas']['totales']))}")
    p.drawString(125, 325, "Valor de cuota")
    p.drawString(350, 325, f"$ {formatNumber(str(datos['datas']['cuota']))}")
    p.drawString(125, 310, "Descuento Maximo")
    p.drawString(350, 310, f"$ {formatNumber(str(datos['datas']['capacidad']))}")
    p.drawString(125, 295, "Monto Maximos a Solicitar")
    p.drawString(350, 295, f"$ {formatNumber(str(datos['datas']['montomaximo']))}")
    
    p.setFont("Helvetica-Bold", 13)
    p.drawString(70, 260, "Requisitos:")
    p.setFont("Helvetica", 9)
    
    text = datos['datas']['requisitos']
    splitText = text.split(" ")
    numberLetter = 0
    listParagraph = []
    paragraph = ""
    for word in splitText:
        paragraph += word + " "
        numberLetter += len(word)
        if numberLetter > 90:
            listParagraph.append(paragraph)
            paragraph = ""
            numberLetter = 0
    if paragraph != "":
        listParagraph.append(paragraph)
    
    pos = 245
    for parag in listParagraph:
        p.drawString(70, pos, parag)
        pos -= 10

    p.setFont("Helvetica-Bold", 13)
    posTitle = pos - 20
    p.drawString(70, posTitle, "Garantias:")
    p.setFont("Helvetica", 9)
    
    text = datos['datas']['garantias']
    splitText = text.split(" ")
    numberLetter = 0
    listParagraph = []
    paragraph = ""
    for word in splitText:
        paragraph += word + " "
        numberLetter += len(word)
        if numberLetter > 90:
            listParagraph.append(paragraph)
            paragraph = ""
            numberLetter = 0
    if paragraph != "":
        listParagraph.append(paragraph)
    
    pos = posTitle - 15
    for parag in listParagraph:
        p.drawString(70, pos, parag)
        pos -= 10
    
    p.setFont("Helvetica-Bold", 14)
    p.drawString(60, 115, "Términos y Condiciones")
    
    condiciones = "Esta simulación está sujeta a verificación de los datos suministrados por el asociado, los cuales a la hora de solicitar el crédito serán presentados por el mismo y revisados por el área de crédito encargada. A su vez estará sujeta a tasas, requisitos, garantías o líneas vigentes por la Cooperativa Contratiempo. A la hora de solicitar el crédito deben cumplirse con todos los reglamentos según el estatuto actual y vigente por la Cooperativa Contratiempo. Este documento da soporte solo a una simulación, lo cual no representa una probación de crédito ya que requiere ser revisado y validado por el área encargada. Algunas líneas de crédito según el monto o tipo del mismo, requerirán de garantías como Codeudores, pago de seguros o aportes."
    splitText = condiciones.split(" ")
    numberLetter = 0
    listParagraph = []
    paragraph = ""
    for word in splitText:
        paragraph += word + " "
        numberLetter += len(word)
        if numberLetter > 117:
            listParagraph.append(paragraph)
            paragraph = ""
            numberLetter = 0
    if paragraph != "":
        listParagraph.append(paragraph)
    
    pos = 100
    p.setFont("Helvetica-Oblique", 7)
    for parag in listParagraph:
        p.drawString(60, pos, parag)
        pos -= 10

    
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="test_simulacion.pdf")


# @login_required
# def deudaAporte(request):
#     deudaAportes = DeudaAporte.objects.all()
#     if request.method == 'POST':
#         form = DeudaAporteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/deudaaporte')
#     else:
#         form = DeudaAporteForm()
#     return render(request, 'deudaaporte/deudaaportes.html',
#                   {'deudaaportes': deudaAportes,
#                    'form': form})

# @login_required
# def update_deudaaporte(request, id):
#     deudaaporte = get_object_or_404(DeudaAporte, id=id)

#     if request.method == 'POST':
#         form = DeudaAporteForm(request.POST, instance=deudaaporte)
#         if form.is_valid():
#             form.save()
#             return redirect('/deudaaporte')
#     else:
#         form = DeudaAporteForm(instance=deudaaporte)

#     return render(request, 'deudaaporte/updatedeudaaporte.html', {'form': form})

# @login_required
# def delete_deudaaporte(request, id):
#     """"""
#     deudaaporte = get_object_or_404(DeudaAporte, id=id)
#     deudaaporte.delete()
#     return redirect('/deudaaporte')

# @login_required
# def extracupo(request):
#     extracupos = Extracupo.objects.all()
#     if request.method == 'POST':
#         form = ExtracupoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/extracupos')
#     else:
#         form = ExtracupoForm()
#     return render(request, 'extracupo/extracupos.html',
#                   {'extracupos': extracupos,
#                    'form': form})

# @login_required
# def update_extracupo(request, id):
#     extracupo = get_object_or_404(Extracupo, id=id)
    
#     if request.method == 'POST':
#         form = ExtracupoForm(request.POST, instance=extracupo)
#         if form.is_valid():
#             form.save()
#             return redirect('/extracupos')
#     else:
#         form = ExtracupoForm(instance=extracupo)
    
#     return render(request, 'extracupo/updateextracupo.html', {'form': form})

# @login_required
# def delete_extracupo(request, id):
    # extracupo = get_object_or_404(Extracupo, id=id)
    # extracupo.delete()
    # return redirect('/extracupos')