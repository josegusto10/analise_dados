import collections
import collections.abc

for _nome in ("Iterable", "Mapping", "Sequence"):
    if not hasattr(collections, _nome):
        setattr(collections, _nome, getattr(collections.abc, _nome))

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
import xlrd

PASTA = Path(__file__).resolve().parent
ARQUIVO = PASTA / "Tabela 1.1.2.xls"

REGIOES = ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]
COLUNAS = [
    "local",
    "total",
    "homem",
    "mulher",
    "total_14_29",
    "homem_14_29",
    "mulher_14_29",
    "total_30_49",
    "homem_30_49",
    "mulher_30_49",
    "total_50_59",
    "homem_50_59",
    "mulher_50_59",
    "total_60_mais",
    "homem_60_mais",
    "mulher_60_mais",
]


def ler_tabela(caminho):
    # xlrd 1.2 abre .xls. O pandas recente pede xlrd 2, que não lê esse formato.
    livro = xlrd.open_workbook(str(caminho))
    planilha = livro.sheet_by_name("2022")
    bruto = pd.DataFrame([planilha.row_values(i) for i in range(planilha.nrows)])
    titulo = str(bruto.iloc[0, 0])
    inicio = bruto.index[bruto.iloc[:, 0].astype(str).str.strip() == "Brasil"][0]
    tabela = bruto.iloc[inicio : inicio + 33, :16].copy()
    tabela.columns = COLUNAS
    tabela = tabela.reset_index(drop=True)
    for coluna in COLUNAS[1:]:
        tabela[coluna] = pd.to_numeric(tabela[coluna], errors="coerce")
    return titulo, tabela


st.title("Tabela 1.1.2")
st.caption(
    "Pessoas ocupadas, por sexo e grupo de idade. "
    "Esta planilha não usa as colunas de cor ou raça da Tabela 1.1.1."
)

if not ARQUIVO.exists():
    st.error(f"Arquivo não encontrado: {ARQUIVO.name}")
    st.stop()

titulo, tabela = ler_tabela(ARQUIVO)
st.write(titulo)
st.dataframe(tabela, hide_index=True, use_container_width=True)

st.markdown("---")
st.subheader("Complemento didático")
st.caption(
    "O enunciado pede a pasta, a tabela e o arquivo .py. "
    "O filtro e o gráfico não foram definidos como obrigatórios."
)

opcao = st.selectbox(
    "Recorte da tabela",
    ["Grandes Regiões", "Unidades da Federação", "Brasil", "Tabela inteira"],
)

if opcao == "Grandes Regiões":
    visao = tabela[tabela["local"].isin(REGIOES)].copy()
elif opcao == "Unidades da Federação":
    visao = tabela[~tabela["local"].isin(["Brasil"] + REGIOES)].copy()
elif opcao == "Brasil":
    visao = tabela[tabela["local"] == "Brasil"].copy()
else:
    visao = tabela.copy()

st.dataframe(visao, hide_index=True, use_container_width=True)

longo = visao.melt(
    id_vars="local",
    value_vars=["homem", "mulher"],
    var_name="sexo",
    value_name="horas",
)
fig = px.bar(
    longo,
    x="local",
    y="horas",
    color="sexo",
    barmode="group",
    title="Horas semanais de cuidados e afazeres — pessoas ocupadas",
    labels={"local": "Local", "horas": "Horas por semana", "sexo": "Sexo"},
)
st.plotly_chart(fig, use_container_width=True)
