# Gráficos

`graficos.ipynb` monta os três gráficos da aula a partir dos arquivos em `dados/`:

- horas por região e sexo, com média simples dos recortes de cor ou raça;
- graduação no Brasil, com as colunas `superior`, `ctem` e `educacao_saude`;
- população de 2022 por UF.

As figuras ficam em `saidas/`.

```powershell
python -m jupyter nbconvert --to notebook --execute --inplace "etapa_3/04_graficos/graficos.ipynb"
```
