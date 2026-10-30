# Preparação do deploy

O item do Classroom traz o guia de publicação e não diz qual aplicativo deve ir para o ar. A escolha abaixo é uma recomendação desta preparação, não uma orientação da professora.

## Candidatos

| Aplicativo | Caminho | Comentário |
|---|---|---|
| Padaria | `etapa_3/streamlit_aula1/app.py` | Primeiro app: catálogo e caixa de seleção. |
| Carros | `etapa_3/08_streamlit_carros/app.py` | Catálogo, carrinho, total, pagamento simulado e troco. |
| Tabela 1.1.2 | `etapa_3/exemplo/app.py` | Lê planilha `.xls` e depende de `xlrd`. |

Recomendação: publicar o app de carros. Ele reúne o que a aula de funções extras pede e não depende de planilha nem de `xlrd`.

## Dados para o Streamlit Community Cloud

- Repositório: `josegusto10/analise_dados`
- URL: https://github.com/josegusto10/analise_dados
- Branch: `main`
- Main file path: `etapa_3/08_streamlit_carros/app.py`
- Dependências do app: `streamlit` e `pandas`, listadas em `etapa_3/08_streamlit_carros/requirements.txt`
- O Cloud instala o `requirements.txt` da raiz do repositório. Esse arquivo inclui as bibliotecas das outras atividades. O app de carros não usa Excel.

Não há segredo, senha ou arquivo `.streamlit/secrets.toml`.

## Roteiro, sem publicar daqui

1. Conferir o app localmente: na raiz do repositório, `python -m streamlit run etapa_3/08_streamlit_carros/app.py`.
2. Enviar a branch `main` ao GitHub somente quando isso for pedido. O repositório já existe; não é preciso criar outro nem rodar `git init` dentro da pasta da atividade.
3. Entrar em https://share.streamlit.io com a conta que tem acesso ao repositório.
4. Criar um app novo, escolher `josegusto10/analise_dados`, branch `main` e o main file path acima.
5. Aguardar o build e abrir a URL que o Cloud mostrar.
6. No app publicado, testar adicionar modelo, total, valor insuficiente, valor maior e limpar o carrinho.

## Situação

Preparado, deploy pendente. Não existe URL pública desta atividade. A publicação só pode ser considerada feita depois de abrir a URL real e ver o app funcionando.
