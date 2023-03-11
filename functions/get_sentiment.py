import requests
import json

# Configurando a api de analise de sentinento
url_sa = "https://api.meaningcloud.com/sentiment-2.1"
key_sa = "76dba976cdc2a85a79b3452591793cd0"

def get_sentiment(text):
    payload = {
        'key': key_sa,
        'txt': text,
        'lang': 'pt'  # definir o idioma do texto aqui
    }
    response = requests.post(url_sa, data=payload)
    if response.status_code == 200:
        result = response.json()
        return result['score_tag']
    else:
        return None