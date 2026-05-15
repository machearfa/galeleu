import random
import streamlit as st

ideiaTecn = ["criar um app de entregas com drones super foda", "desenvolver um teclado holografico", "Um carregador solar ultraa rapido e foda"]
categoria = ["tecnologia", "games", "pets", "comidas", "esportes"]
ideiaGames = ["crie algum console", "crie um jogo", "crie um chadres eletronico"]
ideiaPets = ["adote um cachorro", "adote uma arara", "adote um leão bebê de 8 cabeças"]
ideiaComida = ["crie uma hamburgueria", "crie um restaurante japones", "coma um sushi"]
ideiaEsporte = ["concorra no campeonato galichamp", 'ganhe o campeonato galichamp', "vire um jogador profissional e fale que foi pelo galichamp que voce chegou aonde está"]


st.title("gerador de ideias de negocios")

escolha = st.selectbox("qual categoria de negócios você quer", categoria)

if st.button("gerar Ideia"):
    if escolha == "tecnologia":
        ideia_sorteada = random.choice(ideiaTecn)
        st.write(ideia_sorteada)

    if escolha == "games":
        ideia_sorteada = random.choice(ideiaGames)
        st.write(ideia_sorteada)

    if escolha == "pets":
        ideia_sorteada = random.choice(ideiaPets)
        st.write(ideia_sorteada)

    if escolha == "comidas":
        ideia_sorteada = random.choice(ideiaComida)
        st.write(ideia_sorteada)

    if escolha == "esportes":
        ideia_sorteada = random.choice(ideiaEsporte)
        st.write(ideia_sorteada)