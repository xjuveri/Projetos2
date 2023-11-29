# inventario_patrimonial/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Ano, Mes, Pagina

def lista_anos(request):
    anos = Ano.objects.all()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'adicionar_ano':
            novo_ano = request.POST.get('novo_ano')
            Ano.objects.create(ano=novo_ano)
        elif action == 'excluir_ano':
            ano_id = request.POST.get('ano_id')
            Ano.objects.get(id=ano_id).delete()

        return redirect('lista_anos')

    return render(request, 'inventario_patrimonial/lista_anos.html', {'anos': anos})

def lista_meses(request, ano):
    ano_obj = get_object_or_404(Ano, ano=ano)
    meses = Mes.objects.filter(ano=ano_obj)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'adicionar_mes':
            novo_mes = request.POST.get('novo_mes')
            Mes.objects.create(ano=ano_obj, nome=novo_mes)
        elif action == 'excluir_mes':
            mes_id = request.POST.get('mes_id')
            Mes.objects.get(id=mes_id).delete()

        return redirect('lista_meses', ano=ano)

    return render(request, 'inventario_patrimonial/lista_meses.html', {'ano': ano_obj, 'meses': meses})

def lista_paginas(request, ano, mes):
    ano_obj = get_object_or_404(Ano, ano=ano)
    mes_obj = get_object_or_404(Mes, ano=ano_obj, nome=mes)
    paginas = Pagina.objects.filter(mes=mes_obj)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'adicionar_pagina':
            titulo = request.POST.get('titulo')
            bloco_de_notas = request.POST.get('bloco_de_notas')
            Pagina.objects.create(mes=mes_obj, titulo=titulo, bloco_de_notas=bloco_de_notas)
        elif action == 'excluir_pagina':
            pagina_id = request.POST.get('pagina_id')
            Pagina.objects.get(id=pagina_id).delete()

        return redirect('lista_paginas', ano=ano, mes=mes)

    return render(request, 'inventario_patrimonial/lista_paginas.html', {'ano': ano_obj, 'mes': mes_obj, 'paginas': paginas})

def nova_pagina(request, ano, mes):
    ano_obj = get_object_or_404(Ano, ano=ano)
    mes_obj = get_object_or_404(Mes, ano=ano_obj, nome=mes)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        bloco_de_notas = request.POST.get('bloco_de_notas')
        Pagina.objects.create(mes=mes_obj, titulo=titulo, bloco_de_notas=bloco_de_notas)
        return redirect('lista_paginas', ano=ano, mes=mes)

    return render(request, 'inventario_patrimonial/nova_pagina.html', {'ano': ano_obj, 'mes': mes_obj})

def visualizar_pagina(request, pagina_id):
    pagina = get_object_or_404(Pagina, pk=pagina_id)
    return render(request, 'inventario_patrimonial/visualizar_pagina.html', {'pagina': pagina})

def novo_ano(request):
    if request.method == 'POST':
        ano = request.POST.get('ano')
        Ano.objects.create(ano=ano)
        return redirect('lista_anos')

    return render(request, 'inventario_patrimonial/novo_ano.html')

