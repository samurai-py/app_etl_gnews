import pandas as pd

def read_news_csv(data):
    try:
        news = pd.read_csv(data)
        return news
    except FileNotFoundError:
        raise Exception("Arquivo CSV não encontrado")

def save_news_csv(news):
    try:
        news.to_csv('../g1_news.csv', index=False)
    except:
        raise Exception("Erro ao salvar dados no arquivo CSV")