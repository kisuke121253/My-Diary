Projeto Django: Diário Interativo
Descrição
Este projeto é um aplicativo web desenvolvido com Django que permite aos usuários manter um diário interativo, registrar seu humor, criar eventos e gerar relatórios semanais. Além disso, o sistema utiliza a API generativa do Google para fornecer recomendações e análises baseadas no conteúdo do diário e nos registros de humor.

Funcionalidades
Registro e Autenticação de Usuários: Permite aos usuários criarem contas, fazer login e logout.
Diário Interativo: Usuários podem criar, editar e salvar páginas em seu diário.
Registro de Humor: Permite registrar o humor diário e acompanhar as mudanças ao longo do tempo.
Calendário de Eventos: Criação e visualização de eventos.
Relatórios Semanais: Geração de relatórios semanais com base nos registros de humor e eventos.
Análises e Recomendações: Utiliza a API do Google para fornecer análises e recomendações.
Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie um ambiente virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate # Para Linux/Mac
venv\Scripts\activate # Para Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configure o banco de dados:

bash
Copiar código
python manage.py migrate
Crie um superusuário (opcional):

bash
Copiar código
python manage.py createsuperuser
Inicie o servidor:

bash
Copiar código
python manage.py runserver
Estrutura do Projeto
home: Redireciona usuários autenticados para o diário e não autenticados para a página de login.
registro: Página de registro de novos usuários.
login_view: Página de login.
logout_view: Função para logout.
calendario: Exibe o calendário de eventos.
detalhe_evento: Exibe os detalhes de um evento específico.
diario: Página principal do diário do usuário.
salvar_nome_diario: Salva o nome do diário.
salvar_pagina: Salva ou atualiza uma página do diário.
buscar_todas_paginas: Retorna todas as páginas do diário.
editar_diario: Edita o nome do diário.
save_page_count: Salva a contagem de páginas diárias.
get_today_page_count: Retorna a contagem de páginas do dia atual.
create_event: Cria um novo evento.
get_events: Retorna todos os eventos do usuário.
get_recommendations: Fornece recomendações baseadas no conteúdo do diário.
salvar_anotacao: Salva uma anotação.
buscar_anotacoes: Retorna todas as anotações do usuário.
excluir_anotacao: Exclui uma anotação específica.
buscar_por_conteudo: Busca páginas do diário por conteúdo.
salvar_humor: Salva o humor do dia.
acompanhamento_semanal_view: Exibe a página de acompanhamento semanal.
analyze_sentiment: Analisa o sentimento baseado nos registros de humor.
analyze_mood_change: Analisa as mudanças de humor ao longo da semana.
download_pdf_view: Gera e baixa um relatório semanal em PDF.
download_word_view: Gera e baixa um relatório semanal em Word.
consultar_eventos: Consulta e analisa eventos da semana.
list_acompanhamento_semanal: Lista todos os acompanhamentos semanais.
delete_acompanhamento: Deleta um acompanhamento semanal.
add_note: Adiciona uma nota a um evento.
delete_note: Deleta uma nota específica.
view_acompanhamento: Visualiza um acompanhamento semanal específico.
Configuração da API do Google
Para utilizar a API generativa do Google, configure sua chave de API no arquivo de configuração:

python
Copiar código
api_key = 'SUA_CHAVE_DE_API'
genai.configure(api_key=api_key)
Licença
Este projeto está licenciado sob os termos da licença MIT.

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas no repositório.

Contato
Para mais informações, entre em contato com seu-email@exemplo.com.
