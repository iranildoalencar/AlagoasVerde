from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
from .models import Doadores
from .forms import DoadoresForm

# @login_required
def doadores_list(request):
    doador = Doadores.objects.all()
    return render(request, 'listar/list.html', {'doador': doador})

# @login_required
def doadores_create(request):
    form = DoadoresForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('doadores_list')
    return render(request, 'cadastrar/doadores_form.html', {'form': form})

# @login_required
def doadores_update(request, id):
    doador = get_object_or_404(Doadores, pk=id)
    form = DoadoresForm(request.POST or None, request.FILES or None,  instance=doador)

    if form.is_valid():
        form.save()
        return redirect('doadores_list')
    return render(request, 'cadastrar/doadores_form.html', {'form': form})

# @login_required
def doadores_delete(request, id):
    doador = get_object_or_404(Doadores, pk=id)

    if request.method == 'POST':
        doador.delete()
        return redirect('doadores_list')

    return render(request, 'apagar/doador_delete_confirm.html', {'doador': doador})