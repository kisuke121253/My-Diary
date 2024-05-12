from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Diario

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Aqui, você pode redirecionar para a tela de login ou diretamente fazer login o usuário e redirecioná-lo para outra página
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


from django.shortcuts import render, redirect
import whisper
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.http import HttpResponse
import os
import re
from datetime import datetime
from babel.dates import format_date
from django.db.models.functions import TruncDate
from collections import OrderedDict
from itertools import groupby
import itertools
from django.shortcuts import render
import google.generativeai as genai
import textwrap

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Diario, Pagina

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# api_key = 'AIzaSyASEelCOGxux50q-JQIIEoc9fWhxl-0mLE'


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        return redirect('diario')  # Nome da URL para a página do diário
    else:
        return redirect('login')  # Nome da URL para a página de login

def registro(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('diario')  # Substitua 'index' pelo nome da sua view de página inicial
    else:
        form = SignUpForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('diario')  # Substitua 'index' pelo nome da sua view de página inicial
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Usuário ou senha inválidos'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout

from .models import Evento
from django.utils import timezone
import pytz
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localtime, activate
import pytz

@login_required
def calendario(request):
    # Define o fuso horário para São Paulo
    activate(pytz.timezone('America/Sao_Paulo'))

    # Pega todos os eventos
    eventos = Evento.objects.filter(user=request.user)

    # Ajusta os eventos para o fuso horário de São Paulo antes de passar para o template
    eventos_ajustados = []
    for evento in eventos:
        eventos_ajustados.append({
            'id': evento.id,
            'titulo': evento.titulo,
            'data_inicio': localtime(evento.data_inicio).isoformat(),
            'data_fim': localtime(evento.data_fim).isoformat(),
        })

    return render(request, 'calendario.html', {'eventos': eventos_ajustados})

@login_required
def detalhe_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'calendario.html', {'evento': evento})

from django.utils import timezone
from .models import MoodLog

@login_required
def diario(request):
    date_today = timezone.now().date()
    try:
        diario = Diario.objects.get(user=request.user)
        already_submitted = MoodLog.objects.filter(user=request.user, date=date_today).exists()
        context = {
            'diary_name': diario.nome,
            'diarios': Diario.objects.filter(user=request.user).order_by('-data_criacao'),
            'already_submitted': already_submitted  # Adiciona isso ao contexto
        }
    except Diario.DoesNotExist:
        context = {'already_submitted': False}

    return render(request, 'diario.html', context)

@login_required
def salvar_nome_diario(request):
    if request.method == "POST":
        nome_diario = request.POST.get('diary_name')
        diario, created = Diario.objects.get_or_create(user=request.user)
        diario.nome = nome_diario
        diario.save()
        # Redireciona para a página do diário após salvar
        return redirect('diario')
    else:
        # Se não for um POST, simplesmente redireciona para a página de criação do diário
        return redirect('diario')
    

@login_required
@csrf_exempt  # Pode ser necessário ajustar para lidar com CSRF de maneira mais segura em produção
def salvar_pagina(request):
    if request.method == 'POST':
        numero_pagina = request.POST.get('numero_pagina')
        conteudo = request.POST.get('conteudo')
        diario, _ = Diario.objects.get_or_create(user=request.user)  # Assume que cada usuário tem um único diário

        pagina, created = Pagina.objects.update_or_create(
            diario=diario,
            numero_pagina=numero_pagina,
            defaults={'conteudo': conteudo},
        )

        return JsonResponse({'status': 'sucesso'})
    else:
        return JsonResponse({'status': 'falha'}, status=400)
    
@login_required
def buscar_todas_paginas(request):
    try:
        diario = Diario.objects.get(user=request.user)
        paginas = diario.paginas.all().order_by('numero_pagina')
        dados_paginas = [{'numero_pagina': p.numero_pagina, 'conteudo': p.conteudo} for p in paginas]
        return JsonResponse({'status': 'sucesso', 'paginas': dados_paginas})
    except Diario.DoesNotExist:
        return JsonResponse({'status': 'erro', 'mensagem': 'Diário não encontrado'}, status=404)

@login_required
def editar_diario(request, diario_id):
    diario = get_object_or_404(Diario, id=diario_id, user=request.user)  # Garante que o diário pertence ao usuário
    if request.method == 'POST':
        diario.nome = request.POST.get('nome_diario')
        diario.save()
        return redirect('diario')  # Redireciona para a página de listagem de diários ou detalhe
    return render(request, 'editar_diario.html', {'diario': diario})


# views.py

from django.http import JsonResponse
from .models import PageCount
import datetime


@login_required
def save_page_count(request):
    if request.method == 'POST':
        page_count = request.POST.get('page_count')
        today = datetime.date.today()
        existing_count = PageCount.objects.filter(date=today, is_saved=True).first()
        if existing_count:
            return JsonResponse({'status': 'error', 'message': 'Page count already saved for today'}, status=400)
        PageCount.objects.create(count=page_count, date=today, is_saved=True)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

    
def get_today_page_count(request):
    today_count = PageCount.objects.filter(date=datetime.date.today()).first()
    if today_count:
        return JsonResponse({'status': 'success', 'count': today_count.count})
    else:
        return JsonResponse({'status': 'error', 'message': 'No data found'}, status=404)


from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from .models import Evento
from django.utils.dateparse import parse_datetime

import pytz
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.dateparse import parse_datetime
from .models import Evento

@require_POST
@login_required
def create_event(request):
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    data_inicio = request.POST.get('data_inicio')
    data_fim = request.POST.get('data_fim')
    
    # Configurando o fuso horário de São Paulo
    sao_paulo = pytz.timezone('America/Sao_Paulo')

    # Tornando as datas conscientes do fuso horário
    data_inicio = parse_datetime(data_inicio)
    if data_inicio:
        data_inicio = sao_paulo.localize(data_inicio)

    data_fim = parse_datetime(data_fim)
    if data_fim:
        data_fim = sao_paulo.localize(data_fim)
    
    Evento.objects.create(
        user=request.user,
        titulo=titulo,
        descricao=descricao,
        data_inicio=data_inicio,
        data_fim=data_fim
    )
    return redirect('calendario')


from django.core.serializers import serialize
from django.http import JsonResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.utils.timezone import localtime
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localtime, activate
import pytz

@login_required
def get_events(request):
    # Define o fuso horário para São Paulo
    activate(pytz.timezone('America/Sao_Paulo'))

    # Filtra eventos pelo usuário logado
    eventos = Evento.objects.filter(user=request.user)

    # Convertendo datas para o fuso horário de São Paulo e formatando a resposta
    eventos_data = []
    for evento in eventos:
        evento_dict = {
            'id': evento.id,  # Certifique-se de que esta linha está incluída
            'title': evento.titulo,
            'start': localtime(evento.data_inicio).isoformat(),
            'end': localtime(evento.data_fim).isoformat(),
            'notas': list(evento.notas.all().values('id', 'texto', 'criado_em'))
        }
        eventos_data.append(evento_dict)

    return JsonResponse({'eventos': eventos_data})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import google.generativeai as genai
import json 

# Configure a API
api_key = 'AIzaSyASEelCOGxux50q-JQIIEoc9fWhxl-0mLE'
genai.configure(api_key=api_key)

@csrf_exempt
@require_http_methods(["POST"])
def get_recommendations(request):
    try:
        # Certifica-se de que há dados no corpo da requisição
        if not request.body:
            return JsonResponse({'error': 'No data provided'}, status=400)

        # Tenta carregar o JSON
        data = json.loads(request.body)
        
        # Pega o prompt do usuário, adiciona texto padrão antes dele
        user_prompt = data.get('prompt')
        if not user_prompt:
            return JsonResponse({'error': 'Prompt not provided'}, status=400)

        # Formata o prompt para a API
        full_prompt = (
            "Você é um ajudante e deve ser curto e direto, recomende filmes, séries e livros e como eles podem ajudar com o problema"
            f"para ajudarem a pessoa com o seguinte problema: {user_prompt}"
        )

        # Interage com a API da Google
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(full_prompt)
        answer = response.text

        # Retorna a resposta
        return JsonResponse({'message': answer}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Anotacao
import json

@require_http_methods(["POST"])
@login_required
def salvar_anotacao(request):
    try:
        data = json.loads(request.body)
        texto = data['texto']
        
        # Cria uma nova anotação vinculada ao usuário logado
        Anotacao.objects.create(usuario=request.user, texto=texto)
        
        return JsonResponse({'message': 'Anotação salva com sucesso!'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
def buscar_anotacoes(request):
    # Obtém todas as anotações do usuário logado
    anotacoes = Anotacao.objects.filter(usuario=request.user).order_by('-data_criacao')
    # Formata as anotações para JSON
    data = [{'id': anotacao.id, 'texto': anotacao.texto, 'data_criacao': anotacao.data_criacao.strftime('%Y-%m-%d %H:%M')} for anotacao in anotacoes]
    return JsonResponse(data, safe=False)  # 'safe=False' é necessário para permitir listas top-level


@login_required
@require_http_methods(["DELETE"])
def excluir_anotacao(request, anotacao_id):
    try:
        anotacao = Anotacao.objects.get(id=anotacao_id, usuario=request.user)
        anotacao.delete()
        return JsonResponse({'message': 'Anotação excluída com sucesso!'}, status=200)
    except Anotacao.DoesNotExist:
        return JsonResponse({'error': 'Anotação não encontrada.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



from django.db.models import Q

@login_required
def buscar_por_conteudo(request):
    query = request.GET.get('query')
    try:
        diario = Diario.objects.get(user=request.user)
        pagina = diario.paginas.filter(conteudo__icontains=query).first()
        if pagina:
            return JsonResponse({'status': 'sucesso', 'numero_pagina': pagina.numero_pagina})
        else:
            return JsonResponse({'status': 'falha', 'mensagem': 'Texto não encontrado'}, status=404)
    except Diario.DoesNotExist:
        return JsonResponse({'status': 'erro', 'mensagem': 'Diário não encontrado'}, status=404)


from django.shortcuts import redirect
from django.utils import timezone
from .models import MoodLog  # Supondo que você tenha um modelo chamado MoodLog

@login_required
def salvar_humor(request):
    if request.method == 'POST' and request.user.is_authenticated:
        mood = request.POST.get('mood')
        date = timezone.now().date()
        MoodLog.objects.update_or_create(user=request.user, date=date, defaults={'mood': mood})
        return redirect('diario')  # Altere para redirecionar para a página principal do diário
    return redirect('login')  # Ou uma página de erro se necessário

from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import AcompanhamentoSemanal

from django.shortcuts import render, redirect
from datetime import date
from datetime import date, timedelta
from django.db.models import Count

@login_required
def acompanhamento_semanal_view(request):
    nome = request.user.username
    data = date.today().isoformat()
    numero_sessao = get_next_session_number()

    if request.method == 'POST':
        obj = AcompanhamentoSemanal(
            nome=nome,
            data=data,
            numero_sessao=numero_sessao,
            avaliacao_humor=request.POST.get('avaliacao_humor', ''),
            mudancas_humor=request.POST.get('mudancas_humor', ''),
            eventos_semana=request.POST.get('eventos_semana', ''),
            sintomas=request.POST.get('sintomas', ''),
            estrategias_coping=request.POST.get('estrategias_coping', ''),
            observacoes_terapeuta=request.POST.get('observacoes_terapeuta', ''),
            objetivos_proxima_semana=request.POST.get('objetivos_proxima_semana', '')
        )
        obj.save()
        return redirect('acompanhamento')
    else:
        print('erro')

    # Recuperando moods da última semana
    one_week_ago = date.today() - timedelta(days=7)
    moods = MoodLog.objects.filter(
        user=request.user, 
        date__gte=one_week_ago
    ).values('mood').annotate(count=Count('mood'))

    # Criando um dicionário para os moods
    mood_data = {mood['mood']: mood['count'] for mood in moods}

    # Assegurando que todos os moods estejam representados no dicionário, mesmo que sejam zero
    all_moods = ['feliz', 'triste', 'irritado', 'ansioso', 'entusiasmado', 'cansado', 'estressado', 'indiferente', 'esperancoso', 'inspirado']
    for mood in all_moods:
        if mood not in mood_data:
            mood_data[mood] = 0

    # Convertendo os dados para JSON para passar ao template
    mood_data_json = json.dumps(mood_data)

    return render(request, 'relatorio.html', {'nome': nome, 'data': data, 'numero_sessao': numero_sessao, 'mood_data': mood_data_json})

def get_next_session_number():
    # Lógica para determinar o próximo número de sessão
    last_session = AcompanhamentoSemanal.objects.order_by('-numero_sessao').first()
    if last_session:
        return last_session.numero_sessao + 1
    return 1

def calcular_numero_sessao(user):
    # Suponha que esta função calcule corretamente o número da próxima sessão para o usuário
    ultima_sessao = AcompanhamentoSemanal.objects.filter(nome=user.get_full_name()).order_by('-numero_sessao').first()
    if ultima_sessao:
        return ultima_sessao.numero_sessao + 1
    return 1


@csrf_exempt
def analyze_sentiment(request):
    if request.method == 'POST':
        # Recuperando moods da última semana
        one_week_ago = date.today() - timedelta(days=7)
        moods = MoodLog.objects.filter(
            user=request.user, 
            date__gte=one_week_ago
        ).values('mood').annotate(count=Count('mood'))
        
        # Criando um dicionário para os moods
        mood_data = {mood['mood']: mood['count'] for mood in moods}
        
        # Convertendo o dicionário de moods para uma string formatada para análise
        user_input = ", ".join([f"{mood}: {count}" for mood, count in mood_data.items()])
        
        result = process_sentiment_analysis(user_input)
        return JsonResponse({'result': result})
    return JsonResponse({'error': 'Request must be POST.'}, status=400)

def process_sentiment_analysis(user_input):
    # Supondo que 'user_input' é a entrada de texto para a análise
    full_prompt = (
        "Você é um ajudante e deve ser ***CURTO E DIRETO e no formato ABNT***, faça a analise geral e profunda dos humores baseado nos seguintes moods com observações: "
        f" esses são os moods da pessoa: {user_input}"
    )

    # Código para interagir com a API ou modelo de IA
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(full_prompt)
    return response.text

@csrf_exempt
def analyze_mood_change(request):
    if request.method == 'POST':
        one_week_ago = date.today() - timedelta(days=7)
        moods = MoodLog.objects.filter(
            user=request.user,
            date__gte=one_week_ago
        ).order_by('date').values('date', 'mood')

        if not moods:
            return JsonResponse({'error': 'No mood data available for analysis.'}, status=400)

        # Preparando input para a IA
        user_input = ", ".join([f"{mood['date']}: {mood['mood']}" for mood in moods])
        mood_change_description = analyze_mood_changes_with_ai(user_input)
        
        return JsonResponse({'mudancas_humor': mood_change_description})
    else:
        return JsonResponse({'error': 'Request must be POST.'}, status=400)

def analyze_mood_changes_with_ai(user_input):
    # Construindo o prompt para a IA
    full_prompt = (
        "Você é um ajudante e deve ser ***CURTO E DIRETO e no formato ABNT***, faça a analise geral e profunda sobre a mudança de humor no decorrer da semana nos seguintes moods com observações: "
        f" esses são os moods da pessoa: {user_input}"
    )

    # Interagindo com o modelo de IA
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(full_prompt)
    return response.text



@csrf_exempt
@login_required
def consultar_eventos(request):
    if request.method == 'POST':
        data = json.loads(request.body)
       
        hoje = datetime.date.today()
        inicio_semana = hoje - datetime.timedelta(days=hoje.weekday())
        fim_semana = inicio_semana + datetime.timedelta(days=6)
        
        # Filtrando eventos do usuário logado
        eventos = Evento.objects.filter(user=request.user, data_inicio__gte=inicio_semana, data_fim__lte=fim_semana)
        eventos_formatados = [evento.titulo for evento in eventos]
        
        # Preparar o prompt para a IA
        full_prompt = (
            "Você é um ajudante e deve ser ***CURTO E DIRETO e no formato ABNT***, faça a análise geral dos profunda sobre os eventos ocorridos no decorrer da semana da pessoa: "
            f" esses são os eventos da pessoa: {eventos_formatados}"
        )
        
        # Interagindo com o modelo de IA
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(full_prompt)
        analise_ia = response.text  # Ajuste essa linha conforme a estrutura de resposta do seu modelo
        

        return JsonResponse({
            'success': True,
            'eventos': eventos_formatados,
            'analise_ia': analise_ia
        })

    return JsonResponse({'success': False, 'error': 'Invalid request'})


@login_required
def list_acompanhamento_semanal(request):
    acompanhamentos = AcompanhamentoSemanal.objects.all()
    last_report = AcompanhamentoSemanal.objects.filter(nome=request.user.username).order_by('-data').first()

    can_generate_report = True
    days_until_next_report = 0  # Dias até que o próximo relatório possa ser gerado

    if last_report and (timezone.now().date() - last_report.data).days < 7:
        can_generate_report = False
        days_until_next_report = 7 - (timezone.now().date() - last_report.data).days

    return render(request, 'list_acompanhamento.html', {
        'acompanhamentos': acompanhamentos,
        'can_generate_report': can_generate_report,
        'days_until_next_report': days_until_next_report
    })

from django.shortcuts import redirect
from django.contrib import messages

@login_required
def delete_acompanhamento(request, id):
    try:
        acompanhamento = AcompanhamentoSemanal.objects.get(pk=id)
        acompanhamento.delete()
        messages.success(request, 'Acompanhamento deletado com sucesso!')
    except AcompanhamentoSemanal.DoesNotExist:
        messages.error(request, 'Acompanhamento não encontrado.')
    return redirect('acompanhamento') 


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Evento, Nota

@csrf_exempt
@login_required
def add_note(request, event_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        evento = Evento.objects.get(id=event_id, user=request.user)
        nova_nota = Nota(evento=evento, texto=data['texto'])
        nova_nota.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)



@csrf_exempt
@require_POST
def delete_note(request, note_id):
    try:
        nota = Nota.objects.get(id=note_id)
        nota.delete()
        return JsonResponse({'status': 'success'}, status=200)
    except Nota.DoesNotExist:
        return JsonResponse({'status': 'not found'}, status=404)