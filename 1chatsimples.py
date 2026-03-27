#importa as bibliotecas necessarias
import openai
import os


#importar da biblioteca dotenv, os metodos load e find dotenv
from dotenv import load_dotenv, find_dotenv

#finddotenv procura arquivo .env que armazena a api, logo em seguida, o loaddotenv carrega 
#esse arquivo e armazena numa variavel anonima (_)
_ = load_dotenv(find_dotenv())

# a inicialização da openai no meu ambiente de codigo
client = openai.Client()

#Criar a interação que é a pergunta do usuario para o modelo de linguagem
mensagens = [{'role': 'user', 'content': "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}] #pelo usuario, role = user

#Configurar a resposta da LLM
resposta = client.chat.completions.create(
    messages=mensagens,
    model='gpt-5.4',
    #max_tokens=1000,
    temperature=1, #criatividade da resposta do modelo, e é uma regua que vai de 0 a 1
    stream=True #retorna a resposta conforme ela vai sendo construida
)

#estamos criando uma estrutura de laço para retornar os pedaços da resposta da LLM
resposta_completa=''
for stream_resposta in resposta:
    texto = stream_resposta.choices[0].delta.content
    if texto:
        resposta_completa += texto
        print(texto, end="")