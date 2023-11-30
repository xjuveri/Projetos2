# relatorio/urls.py
from django.urls import path
from .views import relatorios_do_mes, relatorio_detalhes, criar_relatorio, meses_do_ano, editar_relatorio

urlpatterns = [
    path('meses/', meses_do_ano, name='meses_do_ano'),
    path('<str:mes>/', relatorios_do_mes, name='relatorios_do_mes'),
    path('<str:mes>/criar_relatorio/', criar_relatorio, name='criar_relatorio'),
    path('relatorio/<int:relatorio_id>/', relatorio_detalhes, name='relatorio_detalhes'),
    path('editar_relatorio/<int:relatorio_id>/', editar_relatorio, name='editar_relatorio'),
]
