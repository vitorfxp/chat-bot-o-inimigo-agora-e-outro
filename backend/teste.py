import requests  

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


print("Digite 'sair' para encerrar a conversa.")
while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Chatbot: Até logo!")
        break

    try:
        resposta = enviar_mensagem(pergunta)
        print("Chatbot:", resposta)
    except Exception as e:
        print("Ocorreu um erro:",e)