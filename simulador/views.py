from django.shortcuts import render
from .forms import UserForm
from .models import DeudaAporte, Extracupo

def simulador(request):
    deudaAporte = DeudaAporte.objects.all()
    extracupo = Extracupo.objects.all()
    return render(request, 'simulador.html', {
        'deudaAporte': deudaAporte,
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