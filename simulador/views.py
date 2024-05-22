from django.shortcuts import render
from .forms import UserForm
from .models import DeudaAporte, Extracupo

def simulador(request):
    deudaAporte = DeudaAporte.objects.all()
    extracupo = Extracupo.objects.all()

    if request.method == 'POST':
        # if DeudaAporte.objects.filter(plazoMin=request.POST.get('typecredit')).exists():
        #     creditType = DeudaAporte.objects.filter(plazoMin=request.POST.get('typecredit'))
        # else:
        #     creditType = Extracupo.objects.filter(plazoMin=request.POST.get('typecredit'))
        datas = {
            'name': request.POST.get('name'),
            'lastname': request.POST.get('lastname'),
            'document': request.POST.get('document'),
            'salario': request.POST.get('salario'),
            'others': request.POST.get('others'),
            'debit': request.POST.get('debit'),
            'years': request.POST.get('years'),
            'score': request.POST.get('score'),
            'typecredit': request.POST.get('typecredit'),
            'monto': request.POST.get('monto'),
            'cuotas': request.POST.get('cuotas'),
            'state': False
        }
        print(datas)
        if len(datas['name']) < 2:
            errors = {
                "name": "Debe tener al menos 2 caracteres"
                }
            return render(request, 'simulador.html', {
                'errors': errors,
                'deudaaporte': deudaAporte,
                'extracupo': extracupo,
                'datas': datas
            })

        datas['state'] = True


        return render(request, 'simulador.html', {
            'datas': datas,
        })

    return render(request, 'simulador.html', {
        'deudaaporte': deudaAporte,
        'extracupo': extracupo
    })



def User(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'asociado.html', {'form': form})