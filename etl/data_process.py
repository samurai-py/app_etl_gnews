import pandas as pd
from functions import get_sentiment
from config.apikey import apikey
import urllib.request
import json

url = f"https://gnews.io/api/v4/search?q=liberdade&lang=pt&country=br&max=10&apikey={apikey}"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))
    articles = data["articles"]

# Processamento de dados    
df = pd.DataFrame(data=articles)
df['news'] = df.apply(lambda row: f'Título: {row["title"]} \n Descrição: {row["description"]}', axis=1)
df['sentiment'] = df['news'].apply(get_sentiment)
df['sentiment'] = df['sentiment'].apply(lambda x: 'NEUTRO' if x == 'NEU' else 'POSITIVO' if x == 'P' else 'NEGATIVO' if x == 'N' else 'Outros')
df_final = df[['news', 'sentiment']]
df_final.to_csv('../g1_news.csv')