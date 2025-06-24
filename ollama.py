import requests

def interroger_ollama(prompt,OLLAMA_MODEL):
    """Fonction bloquante à exécuter dans un thread"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )
        if response.status_code == 200:
            data = response.json()
            return data.get("response", "Aucune réponse reçue.")
        else:
            return f"Erreur HTTP {response.status_code}"
    except Exception as e:
        return f"Erreur lors de la requête : {str(e)}"