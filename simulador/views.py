from django.shortcuts import render
from .forms import UserForm
from .models import DeudaAporte, Extracupo

def simulador(request):
    deudaAporte = DeudaAporte.objects.all()
    extracupo = Extracupo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        document = request.POST.get('document')
        salario = request.POST.get('salario')
        others = request.POST.get('others')
        debit = request.POST.get('debit')
        years = request.POST.get('years')
        score = request.POST.get('score')
        typecredit = request.POST.get('typecredit')
        monto = request.POST.get('monto')
        cuotas = request.POST.get('cuotas')
        # if str(typecredit) == str(deudaAporte['name']):
        #     tasa = deudaAporte['tasa']
        # else:
        tasa = 0
        
        datas = {
            'name': name,
            'lastname': lastname,
            'document': document,
            'salario': salario,
            'others': others,
            'debit': debit,
            'years': years,
            'score': score,
            'typecredit': typecredit,
            'monto': monto,
            'cuotas': cuotas,
            'tasa': tasa,
            'deudaaporte': deudaAporte,
            'extracupo': extracupo,
            'state': True
        }
        
    
        return render(request, 'simulador.html', {
            'datas': datas
        })
    return render(request, 'simulador.html', {
            'deudaaporte': deudaAporte,
            'extracupo': extracupo})


def User(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'asociado.html', {'form': form})