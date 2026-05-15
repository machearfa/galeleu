ideias = {
        "Tecnologia": [
            "App que organiza tarefas escolares",
            "IA para resumir aulas",
            "Site para aprender programação"
        ],

        "Games": [
            "Campeonato online",
            "Loja de skins",
            "Canal de gameplay"
        ],

        "Pets": [
            "Coleira inteligente",
            "Hotel para pets",
            "Rede social de animais"
        ],

        "Comida": [
            "Delivery saudável",
            "Doceria online",
            "App de receitas"
        ],

        "Esportes": [
            "Escolinha online",
            "App de treinos",
            "Ranking de atletas"
        ]
    }

#importar as bibliotecas
import streamlit as st
import random

st.title("GERADOR DE IDEIAS DE NEGÓCIOS")
nome = st.text_input("NOME DO USUÁRIO: ")

categorias = ['Tecnologia', 'Games', 'Pets', 'Comidas', 'Esportes']
escolha = st.selectbox("QUAL CATEGORIA VOCÊ QUER?", categorias )

botao = st.button("CLIQUE PARA GERAR UMA IDEIA")

if botao:
    aleatorio = random.choice(ideias[escolha])
    st.write(f"{aleatorio}")
    st.snow()