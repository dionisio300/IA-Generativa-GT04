import os
import requests
import dotenv

# dotenv.load_dotenv()
# API_KEY = os.getenv('GEMINI_API_KEY')
# modelo = 'gemini-2.5-flash'
# url_base = f"https://generativelanguage.googleapis.com/v1beta/models"
# url = f"{url_base}/{modelo}:generateContent?key={API_KEY}"
# print(url)
# mensagem = input('Faça sua pergunta')
# payload = {
#     "contents":[
#         {
#             "parts":[
#                 {"text":mensagem}
#             ]
#         }
#     ]
# }
# resposta = requests.post(url,json=payload)
# resposta = resposta.json()
# texto_resp = resposta['candidates'][0]['content']['parts'][0]['text']
# print(f'O gemini respondeu: {texto_resp}')

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
                "temperature":0.1,
            }
        }

while True:
    opcao = input('1 - Converse com o atendente\n2 - Sair\nResposta: ')
    if opcao == '1':
        mensagem = input('Digite sua pergunta: ')

        content = { "role":"user","parts":[{"text":mensagem}]}
        payload['contents'].append(content)

        resposta = conversar_gemini(payload=payload)

        resposta_gemini = resposta['candidates'][0]['content']
        payload['contents'].append(resposta_gemini)

        print(f'resposta: {resposta_gemini}')

    elif opcao == '2':
        print('Saindo')
        break
