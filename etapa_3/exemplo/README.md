# Tabela 1.1.2

O enunciado pede a pasta `exemplo`, a planilha, um arquivo `.py` e as bibliotecas `xlrd`, `streamlit` e `plotly`.

`app.py` lê a aba 2022 de `Tabela 1.1.2.xls`, que está nesta pasta. A tabela é de pessoas ocupadas, por sexo e grupo de idade. As colunas não são as da Tabela 1.1.1.

O filtro e o gráfico Plotly são complemento didático. O enunciado não definiu uma visualização obrigatória.

Na raiz do repositório:

```powershell
python -m streamlit run etapa_3/exemplo/app.py
```
