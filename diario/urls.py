"""
URL configuration for diario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from django.urls import path 
from . import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('calendario/', views.calendario, name='calendario'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('calendario/', views.calendario, name='calendario'),
    path('evento/<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
    path('diario/', views.diario, name="diario"),
    path('salvar_nome_diario/', views.salvar_nome_diario, name="salvar_nome_diario"),
    path('salvar_pagina/', views.salvar_pagina, name='salvar_pagina'),
    path('buscar_todas_paginas/', views.buscar_todas_paginas, name='buscar_todas_paginas'),
    path('editar-diario/<int:diario_id>/', views.editar_diario, name='editar_diario'),
    path('save_page_count/', views.save_page_count, name='save_page_count'),
    path('create_event/', views.create_event, name='create_event'),
    path('get_events/', views.get_events, name='get_events'),
    path('get_recommendations/', views.get_recommendations, name='get_recommendations'),
    path('salvar_anotacao/', views.salvar_anotacao, name="salvar_anotacao"),
    path('buscar_anotacoes/', views.buscar_anotacoes, name="buscar_anotacoes"),
    path('excluir_anotacao/<int:anotacao_id>/', views.excluir_anotacao, name='excluir_anotacao'),
    path('buscar_por_conteudo/', views.buscar_por_conteudo, name='buscar_por_conteudo'),
    path('salvar_humor/', views.salvar_humor, name='salvar_humor'),
    path('get_today_page_count/', views.get_today_page_count, name='get_today_page_count'),
    path('acompanhamento/', views.list_acompanhamento_semanal, name='acompanhamento'),
    path('analyze_sentiment/', views.analyze_sentiment, name='analyze_sentiment'),
    path('analyze_mood_change/', views.analyze_mood_change, name='analyze_mood_change'),
    path('consultar_eventos/', views.consultar_eventos, name='consultar_eventos'),
    path('acompanhamento_semanal_view/', views.acompanhamento_semanal_view, name='acompanhamento_semanal_view'),
    path('acompanhamento_semanal/', views.acompanhamento_semanal_view, name='acompanhamento_semanal'),
    path('delete-acompanhamento/<int:id>/', views.delete_acompanhamento, name='delete_acompanhamento'),
    path('add_note/<int:event_id>/', views.add_note, name='add_note'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('download_pdf_view_criar/', views.download_pdf_view_criar, name='download_pdf_view_criar'),
    path('download_word/', views.download_word_view, name='download_word'),
    path('acompanhamentos/download/<int:acompanhamento_id>/', views.download_pdf_view, name='download_pdf_view'),
    path('acompanhamento/<int:id>/', views.view_acompanhamento, name='view_acompanhamento'),
]
