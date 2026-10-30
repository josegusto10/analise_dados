# analise_dados — Python, 3ª etapa

Repositório: https://github.com/josegusto10/analise_dados  
Branch: `main`

A pasta `ATIVIDADE 3 0,5 indicadores + atividade 2 0,5` continua como foi publicada. As atividades novas estão em `etapa_3/`. Os anexos originais estão em `dados/` e os materiais da aula em `referencias/`.

## Como executar

Na raiz deste repositório, com Python 3:

```powershell
python -m pip install -r requirements.txt
```

`xlrd==1.2.0` é a versão que ainda abre arquivo `.xls`. O pandas recente não aceita essa versão dentro de `read_excel`, então os notebooks e o app da Tabela 1.1.2 chamam o `xlrd` direto. No Python 3.10 ou mais novo, o código também ajusta `collections` antes desse import.

Os notebooks procuram a pasta `dados/` a partir do diretório atual, subindo até achar a raiz do repositório. Dá para rodar da raiz ou da pasta da atividade.

```powershell
python -m jupyter nbconvert --to notebook --execute --inplace "etapa_3/01_numpy_series/atividade1_resolvida.ipynb"
python -m streamlit run etapa_3/streamlit_aula1/app.py
python -m streamlit run etapa_3/08_streamlit_carros/app.py
python -m streamlit run etapa_3/exemplo/app.py
```

## Atividades

| Pasta | O que é | Entrada | Saída |
|---|---|---|---|
| [01_numpy_series](etapa_3/01_numpy_series/) | Vetor, matriz e Series | `referencias/Atividade1.ipynb` | `atividade1_resolvida.ipynb` |
| [02_indicadores_mulheres_revisao](etapa_3/02_indicadores_mulheres_revisao/) | Só as cinco diferenças de horas que faltavam | `dados/Tabela 1.1.1.xls` | notebook executado |
| [03_populacao](etapa_3/03_populacao/) | População por UF e por município | planilha do Censo em `dados/` | dois CSV em `saidas/` |
| [04_graficos](etapa_3/04_graficos/) | Gráficos das atividades 2, 3 e 4 | tabelas em `dados/` | três PNG em `saidas/` |
| [05_idh_melt](etapa_3/05_idh_melt/) | IDH, melt e linhas | `dados/Tabela4.csv` | dois PNG em `saidas/` |
| [06_desocupacao_merge](etapa_3/06_desocupacao_merge/) | Merge das Tabelas 5 com as horas | CSV de 2012 e 2026 e a Tabela 1.1.1 | CSV e PNG em `saidas/` |
| [streamlit_aula1](etapa_3/streamlit_aula1/) | Padaria: catálogo e seleção | itens do enunciado | `app.py` |
| [08_streamlit_carros](etapa_3/08_streamlit_carros/) | Carrinho e pagamento simulado | preços de exemplo | `app.py` |
| [09_checklist_funcoes](etapa_3/09_checklist_funcoes/) | Respostas para revisar o Forms | questionário | `RESPOSTAS_PARA_REVISAO.md` |
| [exemplo](etapa_3/exemplo/) | Tabela 1.1.2 no Streamlit | `Tabela 1.1.2.xls` nesta pasta | `app.py` |
| [11_deploy](etapa_3/11_deploy/) | Roteiro de publicação | guia em `referencias/` | `DEPLOY.md` |

## Resultados que os notebooks calcularam

Atividade 1: a Series da Carla é 19, igual à terceira idade. A matriz de exemplo tem shape `(2, 3)` e o elemento `[1, 2]` é 60. O filtro de 21 anos ou mais mantém os rótulos.

Atividade 2, horas por semana, mulher preta ou parda menos o outro grupo: Minas Gerais 0,9 a mais que mulher branca; Brasil 10,3 a mais que homem branco; Amapá 0,7 a menos que mulher branca; Paraná 0,5 a mais que mulher branca. Nas cinco regiões a diferença também é positiva, de 0,3 no Sul a 1,3 no Sudeste.

População: 5.570 municípios, 27 UFs, sem código duplicado e sem população ausente. A soma dos estados fecha com a soma dos municípios. O maior crescimento estadual entre 2010 compatibilizado e 2022 foi São Paulo. Entre municípios, Manaus teve o maior aumento. Há 232 nomes de município repetidos em estados diferentes; a UF e o código separam esses casos. Em 1.623 municípios a sinopse de 2010 difere da coluna compatibilizada, e a conta usa a coluna compatibilizada.

IDH da tabela anexa: 27 estados, sem IDH ausente e sem UF/ano duplicado. Ninguém terminou 2024 abaixo de 1991. A maior melhora nesse intervalo foi Tocantins, 0,428. Os 27 estados tiveram alguma queda entre anos vizinhos da tabela. O gráfico geral usa o eixo de 0,3 a 0,9; o menor valor lido foi 0,357 e o maior 0,87.

Desocupação: as duas Tabelas 5 têm 27 linhas, chaves únicas, e o merge não perdeu nem duplicou estado. Os 27 nomes bateram com as UFs da Tabela 1.1.1. Homem mais mulher soma 100 em todas as linhas. Esse percentual é participação entre desocupados, não taxa de desocupação das mulheres.

## O que ainda depende de outra ação

- O Google Forms do checklist não foi enviado.
- Nenhum app foi publicado. Não há URL do Streamlit Cloud. O candidato sugerido em `etapa_3/11_deploy/DEPLOY.md` é o app de carros.
- Nada foi entregue no Classroom.
- O commit e o push não foram feitos.

O acompanhamento de cada item está em [PROGRESSO.md](PROGRESSO.md). A origem dos anexos está em [FONTES.md](FONTES.md).
