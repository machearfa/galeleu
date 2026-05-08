import random
import streamlit as st

ideiaTecn = ["criar um app de entregas com drones super foda", "desenvolver um teclado holografico", "Um carregador solar ultraa rapido e foda"]
categoria = ["tecnologia", "games", "pets", "comidas", "esportes"]

st.title("gerador de ideias de negocios")

escolha = st.selectbox("qual categoria de negócios você quer", categoria)

if st.button("gerar Ideia"):
    if escolha == "tecnologia":
        ideia_sorteada = random.choice(ideiaTecn)
        st.write(ideia_sorteada)