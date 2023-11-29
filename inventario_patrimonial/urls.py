# inventario_patrimonial/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_anos, name='lista_anos'),
    path('<int:ano>/', views.lista_meses, name='lista_meses'),
    path('<int:ano>/<str:mes>/relatorios/', views.lista_paginas, name='lista_paginas'),
    path('<int:ano>/<str:mes>/nova_pagina/', views.nova_pagina, name='nova_pagina'),
    path('pagina/<int:pagina_id>/', views.visualizar_pagina, name='visualizar_pagina'),
    path('novo_ano/', views.novo_ano, name='novo_ano'),  # Adicione esta linha
    
]
