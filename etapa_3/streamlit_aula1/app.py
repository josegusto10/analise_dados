import pandas as pd
import streamlit as st

st.title("Padaria — primeiros passos")
st.subheader("Catálogo de itens e preços")

itens = [
    "Pão Francês (kg)",
    "Pão de Queijo (un)",
    "Leite Integral (L)",
    "Queijo Mussarela (g)",
    "Presunto (g)",
    "Café Espesso (un)",
    "Bolo de Cenoura (fatia)",
]

precos = [
    14.90,
    2.50,
    5.80,
    12.50,
    9.80,
    6.00,
    8.50,
]

catalogo = pd.DataFrame({"Item": itens, "Preço (R$)": precos})
st.write("Estes são os itens e os preços informados na atividade. Não há quantidade vendida nem faturamento.")
st.dataframe(catalogo, hide_index=True, use_container_width=True)

escolha = st.selectbox("Escolha um item", catalogo["Item"])
preco = catalogo.loc[catalogo["Item"] == escolha, "Preço (R$)"].iloc[0]
st.write(f"Item selecionado: **{escolha}**")
st.write(f"Preço: **R$ {preco:.2f}**")
