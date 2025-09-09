📧 Analisador de Emails com IA — AutoUAPI

Interface web para análise e classificação de emails com Python, Flask e a API do Google Gemini.
Uma solução simples e eficaz para automatizar a triagem de emails, com backend limpo e UX clara. ✨

🚀 Funcionalidades

🔎 Análise de Conteúdo por IA
Utiliza o modelo gemini-1.5-flash-latest para interpretar o teor de um email.

🗂️ Classificação Automática
Categoriza emails em:

📌 Solicitação de Status

📎 Envio de Arquivo

💤 Não Relevante

✍️ Geração de Resposta
Sugere rascunhos de resposta profissionais e contextuais.

⚡ Interface Web Reativa
Frontend simples, com feedback visual durante a análise.

🔐 Configuração Segura
Uso de variáveis de ambiente para gerenciar a chave da API.

🛠️ Tecnologias

Backend: Flask

Linguagem: Python

IA: Google Gemini API

Servidor de Produção: Gunicorn

Frontend: HTML, CSS, JavaScript (vanilla)

Dependências: Pip & Venv

Env Vars: python-dotenv

📂 Estrutura do Projeto
AutoU_teste/
├─ static/           # Arquivos CSS e JS estáticos
│  └─ style.css
├─ templates/        # Templates HTML (renderizados pelo Flask)
│  └─ index.html
├─ venv/             # Ambiente virtual Python
├─ .env              # Variáveis de ambiente (API Key)
├─ .gitignore        # Ignorados pelo Git
├─ app.py            # Lógica principal da aplicação (Flask server)
└─ requirements.txt  # Dependências Python

🏁 Como Rodar Localmente
📌 Pré-requisitos

Python 3.10+

Git

Chave da Google AI Studio

⚙️ Instalação
# Clone o repositório
git clone https://github.com/GuilhermeBuenoReis/AutoU_teste.git
cd AutoU_teste

# Crie o ambiente virtual
python3 -m venv venv

# Ative (Linux/macOS)
source venv/bin/activate
# Ative (Windows)
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

🔑 Configuração

Crie um arquivo .env na raiz do projeto:

GOOGLE_API_KEY="SUA_CHAVE_DE_API_DO_GOOGLE_VEM_AQUI"

▶️ Rodando o servidor
flask run


Acesse em: http://127.0.0.1:5000/

📜 Licença

Projeto desenvolvido para estudo e prática com IA + Flask.
Sinta-se à vontade para usar como base. 🚀
