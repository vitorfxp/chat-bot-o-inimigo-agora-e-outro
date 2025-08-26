from flask import Flask, request, jsonify
from flask_cors import CORS
import requests  # Substitui o httpx (usado no FastAPI)

app = Flask(__name__)
CORS(app, resources={
    r"/chat": {"origins": "*"},
    r"/api/chat": {"origins": "*"}
})  # Habilita CORS para todas as rotas

# Rota principal do chat (simples)
@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200
    
    return jsonify({"message": "Chat response"})

# Rota para integrar com o Ollama (Llama3)
@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def api_chat():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200
    
    try:
        data = request.get_json()
        user_message = data.get("text", "")

        # Requisição para o Ollama (substitui httpx por requests)
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3",
                "messages": [{"role": "user", "content": user_message}]
            },
            timeout=30
        )
        
        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)


