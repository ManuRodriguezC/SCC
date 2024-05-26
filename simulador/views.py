from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, DeudaAporteForm
from .models import DeudaAporte, Extracupo
from django.contrib import messages

def simulador(request):
    deudaAporte = DeudaAporte.objects.all()
    extracupo = Extracupo.objects.all()

    if request.method == 'POST':
        # if DeudaAporte.objects.filter(plazoMin=request.POST.get('typecredit')).exists():
        #     creditType = DeudaAporte.objects.filter(plazoMin=request.POST.get('typecredit'))
        # else:
        #     creditType = Extracupo.objects.filter(plazoMin=request.POST.get('typecredit'))
        data = {
            'name' : request.POST.get('name'),
            'lastname': request.POST.get('lastname'),
            'document': request.POST.get('document'),
            'salario': request.POST.get('salario'),
            'others': request.POST.get('others'),
            'debit': request.POST.get('debit'),
        }
        
        typeCredit = request.POST.get('typecredit1') if request.POST.get('typecredit1') else request.POST.get('typecredit2')
        monto = request.POST.get('monto1') if request.POST.get('monto1') else request.POST.get('monto2')
        cuotas = request.POST.get('cuotas1') if request.POST.get('cuotas1') else request.POST.get('cuotas2')
        
        objectType = DeudaAporte.objects.get(name=typeCredit) if DeudaAporte.objects.get(name=typeCredit) else Extracupo.objects.get(name=typeCredit)
        
        print(objectType)
                
        request.session['form_data'] = data
        
        
        if len(data['name']) < 5:
            messages.error(request, "El nombre debe ser mayor a 5 caracteres")
            return redirect('/')
        if len(data['lastname']) < 8:
            messages.error(request, "El apellido debe ser mayor a 5 caracteres")
            return redirect('/')
            
        del request.session['form_data']
        return redirect('/')


    form_data = request.session.get('form_data', {})
    return render(request, 'simulador.html', {
        'deudaaporte': deudaAporte,
        'extracupo': extracupo,
        'form_data': form_data  # Agrega esto
    })


def deudaAporte(request):
    deudaAportes = DeudaAporte.objects.all()
    if request.method == 'POST':
        form = DeudaAporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/deudaaporte')
    else:
        form = DeudaAporteForm()
    return render(request, 'deudaaporte/deudaaportes.html',
                  {'deudaaportes': deudaAportes,
                   'form': form})
    
def update_deudaaporte(request, id):
    deudaaporte = get_object_or_404(DeudaAporte, id=id)

    if request.method == 'POST':
        form = DeudaAporteForm(request.POST, instance=deudaaporte)
        if form.is_valid():
            form.save()
            return redirect('/deudaaporte')
    else:
        form = DeudaAporteForm(instance=deudaaporte)

    return render(request, 'deudaaporte/updatedeudaaporte.html', {'form': form})

def delete_deudaaporte(request, id):
    """"""
    deudaaporte = get_object_or_404(DeudaAporte, id=id)
    deudaaporte.delete()
    return redirect('/deudaaporte')
    

    