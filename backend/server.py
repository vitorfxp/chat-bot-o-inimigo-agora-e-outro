from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Permitir requisições do frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Em produção, coloque o domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sua função que chama a API Ollama
def enviar_mensagem(mensagem):
    url = "http://localhost:11434/api/chat"  
    payload = {
        "model": "llama3",  
        "messages": [
            {"role": "user", "content": mensagem}
        ],
        "stream": False  
    }
    
    resposta = requests.post(url, json=payload)
    return resposta.json()["message"]["content"]

# Rota do chat que o frontend vai chamar
@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    mensagem = data.get("message")
    resposta = enviar_mensagem(mensagem)
    return {"response": resposta}




