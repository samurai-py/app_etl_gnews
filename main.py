from flask import Flask
from flask import request
from flask import jsonify
from config.apikey import apikey
from functions.files import read_news_csv
from api_func.endpoints import *
import pandas as pd
import json
import urllib.request

app = Flask(__name__)

def fetch_news():
    try:
        url = f"https://gnews.io/api/v4/search?q=liberdade&lang=pt&country=br&max=10&apikey={apikey}"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))
            if data.get("articles"):
                return data["articles"]
            else:
                raise Exception("Erro ao carregar notícias da API")
    except urllib.error.HTTPError as e:
        raise Exception(f"Erro ao carregar notícias da API: {e.reason}")

read_news_csv('g1_news.csv')

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(get_all_data())

@app.route('/data', methods=['POST'])
def add_data():
    data = request.get_json()
    return jsonify(add_new_data(data))

@app.route('/data/<id>', methods=['GET'])
def get_data_by_id(id):
    return jsonify(get_data_by_id(id))

@app.route('/data/<id>', methods=['PUT'])
def update_data(id):
    data = request.get_json()
    return jsonify(update_data(id, data))

@app.route('/data/<id>', methods=['DELETE'])
def delete_data(id):
    return jsonify(delete_data(id))

if __name__ == '__main__':
    try:
        articles = fetch_news()
    except Exception as e:
        print(f"Erro ao carregar notícias da API: {str(e)}")
        articles = []
    app.run()
