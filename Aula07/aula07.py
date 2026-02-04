import os
import requests
import dotenv

dotenv.load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')
modelo = 'gemini-2.5-flash'
url_base = f"https://generativelanguage.googleapis.com/v1beta/models"
url = f"{url_base}/{modelo}:generateContent?key={API_KEY}"
print(url)


mensagem = input('Faça sua pergunta')
payload = {
    "contents":[
        {
            "parts":[
                {"text":mensagem}
            ]
        }
    ]
}
resposta = requests.post(url,json=payload)
resposta = resposta.json()

texto_resp = resposta['candidates'][0]['content']['parts'][0]['text']

print(f'O gemini respondeu: {texto_resp}')
