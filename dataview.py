import streamlit as st
import pandas as pd
from supabase import create_client, Client
import json

# Configurações do Supabase
SUPABASE_URL = ""
SUPABASE_KEY = ""

# Função para conectar ao Supabase
def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

# Função para buscar dados da tabela
def fetch_data_from_supabase(supabase: Client, table_name: str):
    response = supabase.table(table_name).select("*").execute()
    data = response.data
    if not data:
        st.write(f"Nenhum dado encontrado na tabela: {table_name}")
        return None
    return pd.DataFrame(data)

# Função para normalizar e processar a coluna 'data_linha'
def process_data(df):
    if "data_linha" in df.columns:
        # Normaliza os dados da coluna 'data_linha' (JSON)
        df_expanded = pd.json_normalize(df['data_linha'])
        df_combined = pd.concat([df.drop(columns=['data_linha']), df_expanded], axis=1)
        return df_combined
    else:
        st.write("A coluna 'data_linha' não foi encontrada no dataframe.")
        return df

# Inicia o Streamlit
def main():
    st.title("Visualização de Dados: Filmes da Marvel")

    # Conectar ao Supabase
    supabase_client = get_supabase_client()

    # Nome da tabela no Supabase
    table_name = "vanderlei"

    # Buscar dados do Supabase
    df = fetch_data_from_supabase(supabase_client, table_name)

    # Se houver dados, exibi-los
    if df is not None:
        # Processa os dados da coluna 'data_linha'
        df_processed = process_data(df)

        # Exibe os dados em uma tabela
        st.write("Dados da Tabela de Filmes:")
        st.dataframe(df_processed)

        # Visualização gráfica: Exemplo de gráficos para os campos 'year' e 'worldwide gross ($m)'
        st.write("Visualização Gráfica:")

        # Gráfico: Receita global por ano
        if 'year' in df_processed.columns and 'worldwide gross ($m)' in df_processed.columns:
            chart_data = df_processed[['year', 'worldwide gross ($m)']].groupby('year').sum()
            st.bar_chart(chart_data)

        # Gráfico: Comparação entre 'critics % score' e 'audience % score'
        if 'critics % score' in df_processed.columns and 'audience % score' in df_processed.columns:
            # Converte percentuais de string para numérico, removendo o símbolo '%'
            df_processed['critics % score'] = df_processed['critics % score'].str.replace('%', '').astype(float)
            df_processed['audience % score'] = df_processed['audience % score'].str.replace('%', '').astype(float)

            score_comparison = df_processed[['movie', 'critics % score', 'audience % score']]
            st.write("Comparação de Pontuação - Críticos vs Audiência:")
            st.dataframe(score_comparison)

            st.line_chart(score_comparison.set_index('movie'))

if __name__ == "__main__":
    main()
