# Progresso — 3ª etapa

Atualizado em 30/10/2026. Repositório `josegusto10/analise_dados`, branch `main`, ainda sem commit destas alterações.

A pasta conjunta não foi modificada.

| Atividade | Implementado | Executado | Resultado | Pendência |
|---|---|---|---|---|
| 01 NumPy e Series | `etapa_3/01_numpy_series/atividade1_resolvida.ipynb` | Notebook inteiro, kernel limpo | Carla = 19 e é a terceira idade. Matriz `(2, 3)`, elemento `[1, 2]` = 60 | Nenhuma de código |
| 02 Indicadores | `questoes_faltantes.ipynb` e `REVISAO.md` | Notebook inteiro | Cinco diferenças calculadas na aba 2022. Amapá ficou negativa | Não reenviar nem mudar o Classroom |
| 03 População | `populacao.ipynb` | Notebook inteiro e releitura dos CSV | 27 UFs, 5.570 municípios, ordenação decrescente conferida | Nenhuma de código |
| 04 Gráficos | `graficos.ipynb` | Notebook inteiro | Três PNG em `saidas/` | Nenhuma de código |
| 05 IDH | `idh.ipynb` | Notebook inteiro | Tocantins +0,428 de 1991 a 2024. Nenhuma queda nesse intervalo. Quedas intermediárias em 27 UFs | Nenhuma de código |
| 06 Desocupação | `desocupacao.ipynb` | Notebook inteiro e releitura do CSV | Merge 27 com 27, sem estado perdido | Nenhuma de código |
| Padaria | `streamlit_aula1/app.py` | AppTest: 7 itens e as 7 opções | Seleção sem exceção | Não publicado |
| Carros | `08_streamlit_carros/app.py` | AppTest: vazio, 2 SUV, falta, troco e limpar | Total R$ 190.000, troco R$ 10.000, carrinho zerou | Não publicado |
| Checklist | `RESPOSTAS_PARA_REVISAO.md` | Leitura das 40 questões | Respostas preparadas | Formulário não enviado |
| exemplo | `exemplo/app.py` e a Tabela 1.1.2 | AppTest: 33 linhas, 16 colunas, filtro de 27 UFs e um gráfico | Filtro e gráfico são complemento | Não publicado |
| Deploy | `DEPLOY.md` | Arquivos do app de carros conferidos | Preparado | Deploy pendente. Sem URL |

## Verificações feitas

- Notebooks executados com `nbclient` e o kernel `cotemig312`, cada um do início ao fim.
- CSV de população relido: 27 e 5.570 linhas, colunas esperadas, ordenação decrescente.
- CSV cruzado da desocupação relido: 27 linhas.
- PNG gerados nas pastas `saidas/`.
- Apps exercitados com `streamlit.testing.v1.AppTest`, não só importados.
- `git status` mostra a pasta conjunta intacta e o restante como arquivo novo.

## Bloqueios que foram contornados na execução local

- Não havia Python no PATH. A execução usou um Python 3.12 embutido no perfil do usuário. Quem for rodar de novo pode usar o Python da máquina, desde que instale `requirements.txt`.
- O pandas 3.1 recusa `engine="xlrd"` com o xlrd 1.2. A leitura do `.xls` ficou no `xlrd.open_workbook`.
- `Tabela4.csv` está em Windows-1252, não em UTF-8. O notebook usa `encoding="cp1252"`.

## Não feito

- Commit, push, publicação no Streamlit e entrega no Classroom.
- Envio do Google Forms.
- Abertura de uma URL pública. Deploy continua pendente.
