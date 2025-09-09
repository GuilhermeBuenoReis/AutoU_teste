Analisador de Emails com IA — Case Prático AutoU

API e interface web para análise e classificação de emails, construída com Python, Flask e a API do Google Gemini. O projeto foi desenhado para ser uma solução simples e eficaz para automatizar a triagem de emails, com foco em uma experiência de usuário clara e uma implementação de backend limpa.
✨ Funcionalidades

    Análise de Conteúdo por IA: Utiliza o modelo gemini-1.5-flash-latest para interpretar o teor de um email.

    Classificação Automática: Categoriza emails em Solicitação de Status, Envio de Arquivo ou Não Relevante.

    Geração de Resposta: A IA sugere um rascunho de resposta profissional e contextualmente apropriada.

    Interface Web Reativa: Frontend simples com feedback visual de carregamento durante a análise.

    Configuração Segura: Gerenciamento de chaves de API através de variáveis de ambiente.

🚀 Tecnologias Principais

    Framework Backend: Flask

    Linguagem: Python

    Inteligência Artificial: Google Gemini API

    Servidor de Produção: Gunicorn

    Frontend: HTML, CSS, JavaScript (vanilla)

    Gerenciamento de Dependências: Pip & Venv

    Variáveis de Ambiente: python-dotenv

📂 Estrutura do Projeto

A estrutura de pastas foi organizada para separar claramente as responsabilidades da aplicação (lógica, templates e arquivos estáticos).

AutoU_teste/
├─ static/           # Arquivos CSS e JS estáticos
│  └─ style.css
├─ templates/        # Templates HTML (renderizados pelo Flask)
│  └─ index.html
├─ venv/             # Ambiente virtual Python
├─ .env              # Arquivo para variáveis de ambiente (chave de API)
├─ .gitignore        # Arquivos e pastas a serem ignorados pelo Git
├─ app.py            # Lógica principal da aplicação (servidor Flask)
└─ requirements.txt  # Lista de dependências Python

🏁 Começando

Siga os passos abaixo para configurar e rodar o projeto localmente.
Pré-requisitos

    Python (v3.10 ou superior)

    Git

    Uma chave de API do Google AI Studio.

Instalação

    Clone o repositório:

    git clone [https://github.com/GuilhermeBuenoReis/AutoU_teste.git](https://github.com/GuilhermeBuenoReis/AutoU_teste.git)
    cd AutoU_teste

    Crie e ative um ambiente virtual:

    # Criar
    python3 -m venv venv
    # Ativar (Linux/macOS)
    source venv/bin/activate

    Instale as dependências:

    pip install -r requirements.txt

    Configure as variáveis de ambiente:
    Crie o arquivo .env na raiz do projeto e adicione sua chave.

    GOOGLE_API_KEY="SUA_CHAVE_DE_API_DO_GOOGLE_VEM_AQUI"

    Inicie o servidor de desenvolvimento:

    flask run

