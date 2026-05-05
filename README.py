import pandas as pd 
df = pd.read_csv
import pandas as pd

df.columns = df.columns.str.strip().str.lower()

df = df.rename(columns={
    "qt_votos": "votos",
    "ds_genero": "sexo",
    "nm_candidato": "nome"
})

# 3. Pegar os mais votados (top 10)
top = df.sort_values(by="votos", ascending=False).head(10)

# 4. Mostrar os mais votados
print("Top 10 deputados mais votados:")
print(top[["nome", "votos", "sexo"]])

# 5. Contar homens vs mulheres
contagem = top["sexo"].value_counts()
print("\nContagem por gênero:")
print(contagem)

# 6. Descobrir maioria
maioria = contagem.idxmax()
print("\nMaioria entre os mais votados:", maioria)
