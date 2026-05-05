import streamlit as st
import pandas as pd

st.title("Análise de Deputados 2018 🗳️")

# Upload do arquivo
arquivo = st.file_uploader("Envie seu CSV", type=["csv"])

if arquivo is not None:
    df = pd.read_csv(arquivo)

    # Limpar nomes das colunas (forma segura)
    df.columns = [str(col).strip().lower() for col in df.columns]

    st.write("Colunas encontradas:", df.columns)

    # AJUSTE AQUI conforme seu dataset
    df = df.rename(columns={
        "qt_votos": "votos",
        "ds_genero": "sexo",
        "nm_candidato": "nome"
    })

    # Verifica se deu certo
    if "votos" in df.columns and "sexo" in df.columns:
        
        # Top 10
        top = df.sort_values(by="votos", ascending=False).head(10)

        st.subheader("Top 10 mais votados")
        st.dataframe(top[["nome", "votos", "sexo"]])

        # Contagem
        contagem = top["sexo"].value_counts()

        st.subheader("Distribuição por gênero")
        st.write(contagem)

        maioria = contagem.idxmax()
        st.success(f"Maioria: {maioria}")

    else:
        st.error("Não encontrei as colunas de votos ou sexo ")
