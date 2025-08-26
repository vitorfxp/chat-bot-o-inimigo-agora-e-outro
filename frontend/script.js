async function sendMessage() {
    const userInput = document.getElementById('user-input').value.trim();
    if (!userInput) return;

    try {
        const response = await fetch('http://localhost:8000/api/chat', {
            method: 'POST',  
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: userInput })
        });

        if (!response.ok) throw new Error(`Erro: ${response.status}`);
        const data = await response.json();
        console.log("Resposta:", data);
        
    } catch (error) {
        console.error("Falha na requisição:", error);
    }
}