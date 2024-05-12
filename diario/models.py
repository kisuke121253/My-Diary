from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class Diario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(default=timezone.now)
    

class Pagina(models.Model):
    diario = models.ForeignKey(Diario, related_name='paginas', on_delete=models.CASCADE)
    numero_pagina = models.IntegerField()
    conteudo = models.TextField(blank=True)

    class Meta:
        unique_together = ['diario', 'numero_pagina']

    def __str__(self):
        return f"Pagina {self.numero_pagina} do {self.diario.nome}"

class Evento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona cada evento a um usuário
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    def __str__(self):
        return self.titulo

class Nota(models.Model):
    evento = models.ForeignKey(Evento, related_name='notas', on_delete=models.CASCADE)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:50]  # Retorna os primeiros 50 caracteres do texto

class PageCount(models.Model):
    count = models.IntegerField()
    date = models.DateField()
    
class Anotacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='anotacoes')
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Anotação de {self.usuario.username} em {self.data_criacao.strftime('%d/%m/%Y %H:%M:%S')}"
    

from django.db import models
from django.contrib.auth.models import User

class MoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    mood = models.CharField(max_length=100)  # ou um choice field se preferir

    def __str__(self):
        return f"{self.user}'s mood on {self.date}: {self.mood}"


from django.db import models

class AcompanhamentoSemanal(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    numero_sessao = models.IntegerField()
    avaliacao_humor = models.CharField(max_length=50)
    mudancas_humor = models.TextField()
    eventos_semana = models.TextField()
    sintomas = models.JSONField()
    estrategias_coping = models.JSONField()
    observacoes_terapeuta = models.TextField()
    objetivos_proxima_semana = models.TextField()

    def __str__(self):
        return self.nome
