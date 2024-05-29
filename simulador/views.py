from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DeudaAporteForm, ExtracupoForm, SalaryForm
from .models import DeudaAporte, Extracupo, Salary
from django.contrib import messages

def simulador(request):
    deudaAporte = DeudaAporte.objects.all()
    extracupo = Extracupo.objects.all()

    if request.method == 'POST':
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
        
        if DeudaAporte.objects.filter(name=typeCredit).exists():
            currentType = DeudaAporte.objects.get(name=typeCredit)
        else:
            currentType = Extracupo.objects.get(name=typeCredit)
                
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

@login_required
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

@login_required
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

@login_required
def delete_deudaaporte(request, id):
    """"""
    deudaaporte = get_object_or_404(DeudaAporte, id=id)
    deudaaporte.delete()
    return redirect('/deudaaporte')

@login_required
def extracupo(request):
    extracupos = Extracupo.objects.all()
    if request.method == 'POST':
        form = ExtracupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/extracupos')
    else:
        form = ExtracupoForm()
    return render(request, 'extracupo/extracupos.html',
                  {'extracupos': extracupos,
                   'form': form})

@login_required
def update_extracupo(request, id):
    extracupo = get_object_or_404(Extracupo, id=id)
    
    if request.method == 'POST':
        form = ExtracupoForm(request.POST, instance=extracupo)
        if form.is_valid():
            form.save()
            return redirect('/extracupos')
    else:
        form = ExtracupoForm(instance=extracupo)
    
    return render(request, 'extracupo/updateextracupo.html', {'form': form})

@login_required
def delete_extracupo(request, id):
    extracupo = get_object_or_404(Extracupo, id=id)
    extracupo.delete()
    return redirect('/extracupos')

def salary(request):
    currentSalary = Salary.objects.all()
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return
    