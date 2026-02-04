import os
import dotenv
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configurações básicas (em produção, use variáveis de ambiente)
app.config['SECRET_KEY'] = 'dev-key-123'

# --- ROTAS INTERNAS ---


# Helpers

def conversar_gemini(modelo='gemini-2.5-flash',payload=''):
    dotenv.load_dotenv()
    API_KEY = os.getenv('GEMINI_API_KEY')
    url_base = f"https://generativelanguage.googleapis.com/v1beta/models"
    url = f"{url_base}/{modelo}:generateContent?key={API_KEY}"
    resposta = requests.post(url,json=payload)
    resposta = resposta.json()
    # texto_resp = resposta['candidates'][0]['content']['parts'][0]['text']
    return resposta



import datetime

hora_atual = datetime.datetime.now()

print(f'Hora atual: {hora_atual.hour}:{hora_atual.minute}')
payload = {
            "systemInstruction":{"parts":[
                {
                    "text": f"Você é um atendente virtual de uma lanchonete. Regras: - Fale sempre em português - Seja educado e objetivo - Faça apenas uma pergunta por vez - Não crie promoções - Sempre confirme o pedido antes de finalizar - Se faltar alguma infomação pergunte e não suponha - O horário de funcionamento da loja é de 18 as 00:00 - A hora agora é {hora_atual.hour}:{hora_atual.minute}"
                    }
                ]},
            "contents":[],
            "generationConfig":{
                "maxOutputTokens":200,
                "temperature":1,
            }
        }


@app.route('/')
def index():
    """Rota principal que carrega a interface do chatbot."""
    return render_template('index.html')

@app.route('/enviar_mensagem', methods=['POST'])
def enviar_mensagem():
    dados = request.get_json()
    mensagem_usuario = dados.get('mensagem', '')

    if not mensagem_usuario:
        return jsonify({"resposta": "Mensagem vazia", "status": "erro"}), 400

    # 1. Adiciona mensagem do usuário ao histórico (Global Payload)
    content_usuario = {"role": "user", "parts": [{"text": mensagem_usuario}]}
    payload['contents'].append(content_usuario)

    # 2. Chama a API
    resposta_json = conversar_gemini(payload=payload)

    # 3. Validação robusta da resposta
    if resposta_json and 'candidates' in resposta_json:
        try:
            # Extrai o conteúdo e o texto especificamente
            conteudo_ia = resposta_json['candidates'][0]['content']
            texto_ia = conteudo_ia['parts'][0]['text']
            
            # Adiciona a resposta da IA ao histórico (Role deve ser 'model')
            payload['contents'].append(conteudo_ia)

            return jsonify({
                "resposta": texto_ia,
                "status": "sucesso"
            })
        except (KeyError, IndexError) as e:
            print(f"Erro ao processar estrutura do JSON: {e}")
            return jsonify({"resposta": "Erro ao processar resposta da IA.", "status": "erro"}), 500
    else:
        # Se cair aqui, imprima o erro para saber se é API KEY ou cota
        mensagem_erro = resposta_json.get('error', {}).get('message', 'Erro desconhecido na API')
        print(f"Falha na Resposta: {mensagem_erro}")
        return jsonify({
            "resposta": f"Ops! Tive um problema: {mensagem_erro}",
            "status": "erro"
        }), 500

# --- TRATAMENTO DE ERROS ---

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', erro="Página não encontrada"), 404

if __name__ == '__main__':
    # debug=True permite que o servidor reinicie sozinho ao salvar alterações
    app.run(debug=True, port=5000)