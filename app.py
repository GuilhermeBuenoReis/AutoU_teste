import os
import json
import google.generativeai as genai
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

@app.route('/')
def index():
    return render_template('index.html', email_text="")

@app.route('/analyze-email', methods=['POST'])
def analyze_email():
    email_text = request.form['email_content']

    if not GOOGLE_API_KEY:
        error_message = "ERRO: A chave GOOGLE_API_KEY não foi encontrada no seu arquivo .env."
        return render_template('index.html', error=error_message, email_text=email_text)

    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')

        prompt = f"""
            Analise o seguinte texto de um email e classifique-o em uma das seguintes categorias:
            'Produtivo': Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema).
            'Improdutivo': Mensagens que não requerem ação, como spam, notificações automáticas ou conversas informais.
            
            Depois, gere um rascunho de resposta profissional, caso seja um email produtivo. Se for improdutivo, a sugestão pode ser "Nenhuma ação necessária.".

            Sua resposta DEVE ser um objeto JSON válido, com as chaves "categoria" e "sugestao_resposta".

            Email para análise:
            ---
            {email_text}
            ---
        """

        response = model.generate_content(prompt)
        
        cleaned_response = response.text.replace('```json', '').replace('```', '').strip()
        
        result = json.loads(cleaned_response)
        
        category = result.get('categoria', 'Categoria não encontrada')
        suggestion = result.get('sugestao_resposta', 'Sugestão não encontrada')

        return render_template('index.html', category=category, suggestion=suggestion, email_text=email_text)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        error_message = f"Não foi possível analisar o email. Detalhe do erro: {e}"
        return render_template('index.html', error=error_message, email_text=email_text)

if __name__ == '__main__':
    app.run(debug=True)

