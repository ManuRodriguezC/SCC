from django.shortcuts import render
from .forms import UserForm

def simulador(request):
    return render(request, 'simulador.html')




def User(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'asociado.html', {'form': form})