import pandas as pd
from sqlalchemy import create_engine

# caminho do CSV (IMPORTANTE: formato Linux)
caminho_csv = "/home/eduardo/documentos/pipelines_dados_politica/database/deputados_2026_id_legis_57.csv"

# ler CSV
df = pd.read_csv(caminho_csv)

# conexão com PostgreSQL
engine = create_engine("postgresql://eduardo:Mateus.3105@localhost:5432/deputados_federais")

# subir dados
df.to_sql("deputados_legislatura_57", engine, if_exists="replace", index=False)

print("Upload concluído com sucesso 🚀")