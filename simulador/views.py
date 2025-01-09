from .forms import SalaryForm, SocialesRetencionForm, SocialesForm, ExtraForm, TasasForm, ContactForm
from .models import Salary, SocialesRetencion, Sociales, Extra, Tasas
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .scoreInterno import calculateInterScore
from django.core.mail import EmailMessage
from .formatNumber import formatNumber
from .pagoMensual import pagoMensual
from django.http import FileResponse
from django.contrib import messages
from .generatePDF import createPdf
import datetime


def simulador(request):
    socialesRetencion = SocialesRetencion.objects.all()
    sociales = Sociales.objects.all()
    extras = Extra.objects.all()
    
    montoMaximoEducacion12 = 20000000
    montoMaximoEducacion24 = 60000000
    montoMaximoCrediSalud = 7000000
    montoMaximoCreditoTemporada = 8000000
    montoMaximoCrediExpress = 10000000
    
    salarioMinimo = Salary.objects.all()
    currentSalari = salarioMinimo[0].value.replace(".", "")
    
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
        score = None
        scoreInterno = None
        descuento = 50
    
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
                tipocredito = "extracupo"
                currentType = Extra.objects.get(name=typeCredit)
                if int(cuotas) > int(currentType.plazoMax):
                    messages.error(request, f"El plazo máximo de cuotas para la linea {currentType.name} es {currentType.plazoMax}.")
                    return redirect('/')
                typeperson = request.POST.get('typeperson')
                if typeperson == "Pensionado Libranza":
                    descuento = 50
                if typeperson == "Empleado o pensionado Ventanilla" or typeperson == "Independiente":
                    scoreInterno = calculateInterScore(request)
                    
                tasas = Tasas.objects.filter(name=typeperson)
                score = request.POST.get('score')
                if int(score) > 1000 or int(score) <= 0:
                    messages.error(request, f"El rango de score debe estar entre 1 y 1000")
                    return redirect('/')
                tasa = 0
                for d in tasas:
                    if int(score) >= float(d.scoreMin) and int(score) <= float(d.scoreMax):
                        plazoMax = d.plazoMax
                        tasa = float(d.tasa)
                if tasa == 0:
                    messages.error(request, f"Su score no aplica para solicitar un credito.")
                    return redirect('/')

        request.session['form_data'] = data
        
        # montoMaximoCredit = int(currentSalari.replace(".", "")) * currentType.montoMax
        if int(cuotas) > int(plazoMax):
            messages.error(request, f"El plazo máximo de cuotas es {plazoMax}.")
            return redirect('/')
        
        ingresosSalario = int(data['salario'].replace(".", ""))
        seguridadSocial = (ingresosSalario * 8) / 100
        ingresosOtros = int(data['others'].replace(".", ""))
        egresos = int(data['debit'].replace(".", ""))
        ingresosTotales = ingresosSalario + ingresosOtros - seguridadSocial
        
        capacidadPago = int((ingresosTotales * (descuento / 100)) - egresos)
        
        montoMensual = pagoMensual(monto, tasa, cuotas)
        
        montoMax = int((int(monto.replace(".", "")) * capacidadPago) / montoMensual)

        if tipocredito == "socialretencion":
            montoMax = montoMaximoCredit

        if tipocredito != "socialretencion":
            controlsEducacion = [
                "Educacion Formal", "Educacion No Formal",
            ]
            if (currentType.name in controlsEducacion):
                if (int(cuotas) <= 12 and int(monto.replace(".", "")) > montoMaximoEducacion12):
                    messages.error(request, f"El monto máximo para esta linea a este numero de cuotas es $ {formatNumber(montoMaximoEducacion12)}")
                    return redirect('/')
                elif ((int(cuotas) > 12 and int(cuotas) <= 24) and int(monto.replace(".", "")) > montoMaximoEducacion24):
                    messages.error(request, f"El monto máximo para esta linea a este numero de cuotas es $ {formatNumber(montoMaximoEducacion24)}")
                    return redirect('/')

            if (currentType.name == "Credisalud" and (int(cuotas) >= 6 and int(cuotas) <= 48) and int(monto.replace(".", "")) > montoMaximoCrediSalud):
                messages.error(request, f"El monto máximo para esta linea a este numero de cuotas es $ {formatNumber(montoMaximoCrediSalud)}")
                return redirect('/')
        
            if (tipocredito == "extracupo"):
                setMonto = int(monto.replace(".", ""))
                if (currentType.name == "Anticipo de Prima" and setMonto > int(ingresosSalario * 0.8)):
                    messages.error(request, f"El monto máximo de anticipo Prima es de $ {formatNumber(int(ingresosSalario * 0.8))}")
                    return redirect('/')
                if (currentType.name == "Anticipo de Sueldo" and setMonto > int(ingresosSalario * 0.45)):
                    messages.error(request, f"El monto máximo de anticipo Sueldo es de $ {formatNumber(int(ingresosSalario * 0.45))}")
                    return redirect('/')
                if currentType.name == "Credito de Temporada" and setMonto > montoMaximoCreditoTemporada:
                    messages.error(request, f"El monto máximo de Crédito de Temporada es de $ {formatNumber(montoMaximoCreditoTemporada)}")
                    return redirect('/')
                if currentType.name == "CrediExpress" and setMonto > montoMaximoCrediExpress:
                    messages.error(request, f"El monto máximo de CrediExpress es de $ {formatNumber(montoMaximoCrediExpress)}")
                    return redirect('/')
                if currentType.name == "Credito de Bienvenida":
                    if typeperson == "Independiente":
                        if setMonto > (int(currentSalari) * 2):
                            messages.error(request, f"El monto máximo de Credito de Bienvenida para Independiente es de $ {formatNumber(int(currentSalari) * 2)}")
                            return redirect('/')
                    else:
                        if setMonto > ingresosSalario:
                            messages.error(request, f"El monto máximo de Credito de Bienvenida para Pensionados e Empleados es de $ {formatNumber(ingresosSalario)}")
                            return redirect('/')
                else:
                    if (capacidadPago <= 0):
                        messages.error(request, f"No tiene Capacidad de Pago para solicitar un crédito.")
                        return redirect('/')
                    if int(monto.replace(".", "")) > montoMax:
                        number = formatNumber(montoMax)
                        messages.error(request, f"El monto máximo según la capacidad de pago es de $ {number}")
                        return redirect('/')
        

            elif int(monto.replace(".", "")) > montoMax and currentType.name not in ["Anticipo de Prima", "Anticipo de Sueldo"]:
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
            'cuota': montoMensual if montoMensual > 0 else 0,
            'capacidad': capacidadPago if capacidadPago > 0 else 0,
            'montomaximo': montoMax if montoMax > 0 else 0,
            'score': score if score else "No Aplica",
            'scoreInterno': scoreInterno if scoreInterno else "No Aplica"
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
    if not datos:
        return redirect('/')
    return render(request, 'dialog.html', datos)

def envioCorreo(request):
    datos = request.session.get('calculos', {})
    if not datos:
        return redirect('/')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            
            html_message = render_to_string('email.html', {
                'name': f"{datos['datas']['data']['name']} {datos['datas']['data']['lastname']}",
                'phone': phone,
                'email': email,
                'line': datos['datas']['type'],
            })
            buffer = createPdf(datos)
            
            email_message = EmailMessage(
                'Solicitud de Credito',
                html_message,
                'estebanclimb@gmail.com',
                ['manu.rodriguezc.dev@gmail.com', 'lysanchezal@gmail.com']
            )
            email_message.content_subtype = 'html'
            
            time = str(datetime.datetime.now()).split(".")[0]
            email_message.attach(f'simulacion-credtio-{time}.pdf', buffer.read(), 'application/pdf')
            
            email_message.send()
            
            del request.session['calculos']    
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'datos': datos})

def success_page(request):
    return render(request, 'success.html')

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
    time = str(datetime.datetime.now()).split(".")[0]
    buffer = createPdf(datos)
    
    return FileResponse(buffer, as_attachment=True, filename=f'simulacion-credito-{time}.pdf')
