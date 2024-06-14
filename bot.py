import requests
from groq import Groq
import json

client = Groq(
    api_key="<groq api key>",
)

def definir(noticia):

    prompt = noticia
    chat_completion = client.chat.completions.create(
     messages=[
        {
            "role": "user",
            "content": prompt,
        }
     ],
     model="llama3-8b-8192",
     )

    sentimiento = chat_completion.choices[0].message.content
    palabras_positivas = ["POSITIVO", "POSITIVA", "Positiva", "Positivo", "POSITIVA.", "POSITIVO.", "Positiva.", "Positivo.", "positivo", "positiva", "positivo.", "positiva."]
    palabras_negativas = ["NEGATIVO", "NEGATIVA", "Negativo", "Negativa", "NEGATIVO.", "NEGATIVA.", "Negativo.", "Negativa.", "negativo", "negativa", "negativo.", "negativa."]
    palabras_neutras = ["NEUTRO", "NEUTRA", "Neutro", "Neutra", "NEUTRO.", "NEUTRA.", "Neutro.", "Neutra.", "neutro", "neutra", "neutro.", "neutra."]

    for i in range(len(palabras_positivas)):
        if palabras_positivas[i] in sentimiento:
            return "POSITIVA"

    for i in range(len(palabras_negativas)):
        if palabras_negativas[i] in sentimiento:
            return "NEGATIVA"

    for i in range(len(palabras_neutras)):
        if palabras_neutras[i] in sentimiento:
            return "NEUTRA"



api_key = "<cryptocompare api key>"
url = f"https://min-api.cryptocompare.com/data/v2/news/?categories=BNB&api_key={api_key}"
response = requests.get(url)
data = response.json()

urls_negativas = []
urls_positivas = []
urls_neutras = []
urls_imposibles = []

for news_item in data["Data"]:
    sentimiento = definir("Analiza el sentimiento de la siguiente informacion sobre binance coin y clasifícala como positiva, neutra o negativa, si la noticia es positiva devolver POSITIVO, si la noticia es negativa devolver NEGATIVO, si la noticia es neutra devolver NEUTRA:\n\n"+news_item["title"]+"\n"+news_item["body"],)
    if sentimiento == "POSITIVA":
        urls_positivas.append(news_item["url"])
    elif sentimiento == "NEGATIVA":
        urls_negativas.append(news_item["url"])
    elif sentimiento == "NEUTRA":
        urls_neutras.append(news_item["url"])
    elif sentimiento == "IMPOSIBLE":
        urls_imposibles.append(news_item["url"])

print("POSITIVAS")
for i in range(len(urls_positivas)):
    print(urls_positivas[i])

print("\n")
print("NEUTRAS")
for i in range(len(urls_neutras)):
    print(urls_neutras[i])

print("\n")
print("NEGATIVAS")
for i in range(len(urls_negativas)):
    print(urls_negativas[i])
