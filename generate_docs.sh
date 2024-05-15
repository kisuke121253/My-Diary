#!/bin/bash

# Caminho para o diretório do projeto (onde está manage.py)
PROJECT_DIR="/c/Users/komba/OneDrive/Documentos/Projetos/projeto-clinica/diario"

# Caminho para o diretório source onde está o conf.py do Sphinx
SOURCE_DIR="$PROJECT_DIR/source"

# Verificar se o diretório source existe
if [ ! -d "$SOURCE_DIR" ]; then
    echo "O diretório source não foi encontrado em $SOURCE_DIR"
    exit 1
fi

# Navegar para o diretório source
cd "$SOURCE_DIR"

# Atualizar o conf.py com o caminho correto
CONF_FILE="$SOURCE_DIR/conf.py"
if [ -f "$CONF_FILE" ]; then
    sed -i "s|sys.path.insert(0, os.path.abspath('.'))|sys.path.insert(0, os.path.abspath('../..'))|" "$CONF_FILE"
    sed -i "s|os.environ['DJANGO_SETTINGS_MODULE'] = ''|os.environ['DJANGO_SETTINGS_MODULE'] = 'diario.settings'|" "$CONF_FILE"
else
    echo "O arquivo conf.py não foi encontrado em $CONF_FILE"
    exit 1
fi

# Configurar as variáveis de ambiente do Django e preparar o Django
echo "Configuring Django environment..."
export DJANGO_SETTINGS_MODULE=diario.settings
python -c "import sys; import django; print('sys.path:', sys.path); django.setup()"

# Gerar os arquivos de resumo usando sphinx-apidoc (opcional)
echo "Generating summary files with sphinx-apidoc..."
sphinx-apidoc -o "$SOURCE_DIR" "$PROJECT_DIR/diario"

# Compilar a documentação usando sphinx-build
echo "Building documentation..."
sphinx-build -b html "$SOURCE_DIR" "$SOURCE_DIR/_build/html"

# Verificar se a documentação foi gerada com sucesso
BUILD_DIR="$SOURCE_DIR/_build/html"
if [ -d "$BUILD_DIR" ]; then
    echo "Documentação gerada com sucesso em $BUILD_DIR"
else
    echo "Falha ao gerar a documentação"
    exit 1
fi
