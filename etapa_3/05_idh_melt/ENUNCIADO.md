# ATIVIDADE 5 MELT MATPLOTLIB

Consulta: 29/10/2026. Prazo: 22/09/2026.

Atividade
assignment
ATIVIDADE 5 MELT MATPLOTLIB
Data de entrega: 22 de set.
more_vert
Mais opções
Item postado: 22 de set. (editado: 22 de set.)
Estigfend
Não entregue (confirmado na leitura posterior)
Nesta aula você abre a `Tabela4.csv` (IDHM por Unidade da Federação) e desenha um gráfico de linhas com **matplotlib**.

pip install pandas matplotlib


import pandas as pd
import matplotlib.pyplot as plt


**O que vamos ver**

1. Abrir um CSV com `;` e vírgula decimal
2. Limpar colunas vazias
3. Ordene os estados por maior IDH em 2024
4. Qual estado teve a maior melhora de IDH entre os anos de 2024 e 1991?
5. Existe algum estado em que o IDH piorou?
5. Passar a tabela inicial do formato largo para o formato longo (`melt`)
6. Plote apenas Minas Gerais
7. Plotar a evolução do IDH de cada estado

Sintaxe do MELT
anos = [c for c in df.columns if str(c).isdigit()]
print(anos)

id_vars = [c for c in df.columns if c not in anos]
df_longo = df.melt(
    id_vars=id_vars,
    value_vars=anos,
    var_name="Ano",
    value_name="IDH",
)
df_longo["Ano"] = df_longo["Ano"].astype(int)
df_longo["IDH"] = pd.to_numeric(df_longo["IDH"], errors="coerce")
df_longo.head()

Sintaxe Gráfico:
fig, ax = plt.subplots(figsize=(12, 7))

for sigla, grupo in df_longo.groupby("Sigla"):
    grupo = grupo.sort_values("Ano")
    ax.plot(grupo["Ano"], grupo["IDH"], marker="o", markersize=3, linewidth=1.5, label=sigla)

ax.set_title("Evolução do IDH por estado (1991–2024)")
ax.set_xlabel("Ano")
ax.set_ylabel("IDH")
ax.set_ylim(0.3, 0.9)
ax.legend(ncol=3, bbox_to_anchor=(1.02, 1), loc="upper left", title="UF")
fig.tight_layout()
plt.show()
Ver instruções

## Links e anexos

- [Detalhes no Classroom](https://classroom.google.com/c/ODQzNTk4ODcxNTU1/a/ODg2NTE4NTcxNTg5/details)
- [Tabela4.csv](https://drive.google.com/file/d/1Hj0UTM5yZTlozONMw2PAK6CR76ftsKIA/view?usp=classroom_web&authuser=0)
