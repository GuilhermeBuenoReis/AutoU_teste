Analisador de Emails com IA - Case Prático AutoU

Este projeto é uma aplicação web simples desenvolvida como parte do processo seletivo da AutoU. A aplicação utiliza a API do Google Gemini para analisar o conteúdo de emails, classificá-los em categorias predefinidas e sugerir uma resposta apropriada.
✨ Funcionalidades

    Interface Web Simples: Uma página única para colar o texto do email e visualizar a análise.

    Classificação por IA: Utiliza o modelo gemini-1.5-flash-latest para classificar emails em:

        Solicitação de Status

        Envio de Arquivo

        Não Relevante

    Sugestão de Resposta: A IA gera um rascunho de resposta profissional com base no conteúdo do email.

    Design Moderno: Interface com tema escuro e feedback de carregamento para uma melhor experiência do usuário.

🛠️ Tecnologias Utilizadas

    Backend: Python 3, Flask

    Inteligência Artificial: Google Gemini API

    Frontend: HTML, CSS, JavaScript (vanilla)

    Servidor de Produção: Gunicorn

    Gerenciamento de Dependências: Pip, Venv

    Variáveis de Ambiente: python-dotenv

🚀 Como Executar Localmente

Siga as instruções abaixo para configurar e executar o projeto em seu ambiente local.
Pré-requisitos

    Python 3.10+

    Git

    Uma chave de API do Google AI Studio

Passos para Instalação

    Clone o repositório:

    git clone [https://github.com/GuilhermeBuenoReis/AutoU_teste.git](https://github.com/GuilhermeBuenoReis/AutoU_teste.git)
    cd AutoU_teste

    Crie e ative um ambiente virtual:
    Isso isola as dependências do projeto.

    # Criar o ambiente
    python3 -m venv venv

    # Ativar no Linux/macOS
    source venv/bin/activate

    # Ativar no Windows (PowerShell)
    .\venv\Scripts\Activate.ps1

    Instale as dependências:
    O arquivo requirements.txt contém todos os pacotes necessários.

    pip install -r requirements.txt

    Configure as variáveis de ambiente:
    Crie um arquivo chamado .env na raiz do projeto. Adicione sua chave de API do Google nele.

    .env

    GOOGLE_API_KEY="SUA_CHAVE_DE_API_DO_GOOGLE_VEM_AQUI"

    Inicie o servidor Flask:
    Agora, basta executar a aplicação.

    flask run
    # Ou, alternativamente:
    # python3 app.py

    Acesse a aplicação:
    Abra seu navegador e acesse o endereço: http://12f7.0.0.1:5000

🌐 Deploy

A aplicação foi implantada na plataforma Render e pode ser acessada através do seguinte link:

https://autou-teste-35dt.onrender.com
