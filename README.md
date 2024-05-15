# Projeto Django: Diário Pessoal e Acompanhamento de Humor

Este projeto Django permite que os usuários mantenham um diário pessoal, acompanhem seu humor e eventos, e gerem relatórios semanais detalhados.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Views](#views)
  - [Home](#home)
  - [Registro](#registro)
  - [Login](#login)
  - [Logout](#logout)
  - [Calendário](#calendário)
  - [Detalhe do Evento](#detalhe-do-evento)
  - [Diário](#diário)
  - [Salvar Nome do Diário](#salvar-nome-do-diário)
  - [Salvar Página](#salvar-página)
  - [Buscar Todas as Páginas](#buscar-todas-as-páginas)
  - [Editar Diário](#editar-diário)
  - [Salvar Contagem de Páginas](#salvar-contagem-de-páginas)
  - [Obter Contagem de Páginas de Hoje](#obter-contagem-de-páginas-de-hoje)
  - [Criar Evento](#criar-evento)
  - [Obter Eventos](#obter-eventos)
  - [Salvar Anotação](#salvar-anotação)
  - [Buscar Anotações](#buscar-anotações)
  - [Excluir Anotação](#excluir-anotação)
  - [Buscar por Conteúdo](#buscar-por-conteúdo)
  - [Salvar Humor](#salvar-humor)
  - [Acompanhamento Semanal](#acompanhamento-semanal)
  - [Analisar Sentimento](#analisar-sentimento)
  - [Analisar Mudança de Humor](#analisar-mudança-de-humor)
  - [Baixar PDF](#baixar-pdf)
  - [Baixar Word](#baixar-word)
  - [Consultar Eventos](#consultar-eventos)
  - [Listar Acompanhamentos Semanais](#listar-acompanhamentos-semanais)
  - [Excluir Acompanhamento](#excluir-acompanhamento)
  - [Adicionar Nota ao Evento](#adicionar-nota-ao-evento)
  - [Excluir Nota](#excluir-nota)
  - [Visualizar Acompanhamento](#visualizar-acompanhamento)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Contato](#contato)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Crie um ambiente virtual e ative-o:
   ```bash
   python3 -m venv env
   source env/bin/activate  # Para Linux/Mac
   env\Scripts\activate  # Para Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## Uso

Acesse a aplicação em seu navegador:
