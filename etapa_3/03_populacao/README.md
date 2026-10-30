# Atividade 4 — população

`populacao.ipynb` lê `dados/CD2022_Populacao_2010_Compatibilizada_20231222.xlsx`.

A planilha fica em `dados/` para não duplicar o arquivo. O notebook acha essa pasta tanto da raiz quanto desta pasta.

Saídas, com separador `;`:

- `saidas/populacao_por_estado.csv`
- `saidas/populacao_por_municipio.csv`

```powershell
python -m jupyter nbconvert --to notebook --execute --inplace "etapa_3/03_populacao/populacao.ipynb"
```
