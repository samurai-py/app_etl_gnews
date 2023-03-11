from flask import jsonify, request
from functions.files import * 

def get_all_data():
    try:
        news = read_news_csv()
        return jsonify(news.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"message": f"Erro: {str(e)}"}), 500

def add_new_data():
    try:
        news = read_news_csv()
        data = request.json
        news = news.append(data, ignore_index=True)
        save_news_csv(news)
        return jsonify({"message": "Dados adicionados com sucesso."}), 201
    except Exception as e:
        return jsonify({"message": f"Erro: {str(e)}"}), 500

def get_data_by_id(id):
    try:
        news = read_news_csv()
        data = news.loc[news['id'] == id]
        if data.empty:
            return jsonify({"message": "Registro não encontrado."}), 404
        return jsonify(data.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"message": f"Erro: {str(e)}"}), 500

def update_data(id):
    try:
        news = read_news_csv()
        data = request.json
        updated_data = news.loc[news['id'] == id]
        if updated_data.empty:
            return jsonify({"message": "Registro não encontrado."}), 404
        updated_data.update(data)
        save_news_csv(news)
        return jsonify({"message": "Dados atualizados com sucesso."}), 200
    except Exception as e:
        return jsonify({"message": f"Erro: {str(e)}"}), 500

def delete_data(id):
    try:
        news = read_news_csv()
        deleted_data = news.loc[news['id'] == id]
        if deleted_data.empty:
            return jsonify({"message": "Registro não encontrado."}), 404
        news.drop(news[news['id'] == id].index, inplace=True)
        save_news_csv(news)
        return jsonify({"message": "Registro excluído com sucesso."}), 200
    except Exception as e:
        return jsonify({"message": f"Erro: {str(e)}"}), 500