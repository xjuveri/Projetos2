# relatorio/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Relatorio
from datetime import datetime
from calendar import month_name
from django.http import HttpResponseBadRequest
from .models import Relatorio

def meses_do_ano(request):
    meses = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril',
        'Maio', 'Junho', 'Julho', 'Agosto',
        'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]
    return render(request, 'relatorio/meses_do_ano.html', {'meses': meses})

def criar_relatorio(request, mes):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        bloco_notas = request.POST.get('bloco_notas')

        # Use a data atual do sistema
        data = datetime.now()

        relatorio = Relatorio.objects.create(
            titulo=titulo,
            bloco_notas=bloco_notas,
            data=data,
            nome_usuario=request.user.username  # Supondo que você esteja usando autenticação de usuário
        )

        return redirect('relatorios_do_mes', mes=mes)

    # Passe o nome do mês para o contexto
    nome_mes = month_name[int(mes)]
    return render(request, 'relatorio/criar_relatorio.html', {'mes': mes, 'nome_mes': nome_mes})

def relatorios_do_mes(request, mes):
    relatorios = Relatorio.objects.filter(data__month=mes)
    
    # Passe o nome do mês para o contexto
    nome_mes = month_name[int(mes)]
    
    return render(request, 'relatorio/relatorios_do_mes.html', {'relatorios': relatorios, 'mes': mes, 'nome_mes': nome_mes})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Relatorio

def relatorio_detalhes(request, relatorio_id):
    relatorio = get_object_or_404(Relatorio, id=relatorio_id)

    if request.method == 'POST':
        # Adicione esta parte para lidar com a exclusão do relatório
        if 'excluir' in request.POST:
            relatorio.delete()
            return redirect('relatorios_do_mes', mes=relatorio.data.month)

    return render(request, 'relatorio/relatorio_detalhes.html', {'relatorio': relatorio})

def editar_relatorio(request, relatorio_id):
    relatorio = get_object_or_404(Relatorio, id=relatorio_id)

    if request.method == 'POST':
        relatorio.titulo = request.POST.get('titulo')
        relatorio.bloco_notas = request.POST.get('bloco_notas')
        relatorio.save()
        return redirect('relatorios_do_mes', mes=relatorio.data.month)

    return render(request, 'relatorio/editar_relatorio.html', {'relatorio': relatorio})