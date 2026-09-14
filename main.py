import sqlite3
import pandas as pd
import os
from datetime import datetime

# 1. Dados simulados de vendas brutas (caso não exista um arquivo CSV)
def gerar_dados_exemplo():
    data = {
        "id_venda": [101, 102, 103, 104, 105],
        "cliente": ["Ana Silva", "Carlos Souza", "Beatriz Lima", "João Pedro", "Maria Clara"],
        "produto": ["Teclado Mecânico", "Mouse Gamer", "Monitor 24", "Cadeira Office", "Headset USB"],
        "valor_unitario": [250.00, 120.00, 850.00, 600.00, 180.00],
        "quantidade": [2, 1, None, 3, 2],  # Dado nulo para tratamento
        "data_venda": ["2026-01-10", "2026-01-11", "2026-01-11", "2026-01-12", "2026-01-12"]
    }
    df = pd.DataFrame(data)
    df.to_csv("vendas_brutas.csv", index=False)
    print("✓ Arquivo 'vendas_brutas.csv' gerado com sucesso!")

# 2. Processamento e Limpeza dos Dados
def processar_dados():
    print("➜ Lendo e tratando dados de vendas...")
    df = pd.read_csv("vendas_brutas.csv")

    # Tratamento: Preenche quantidades ausentes com 1
    df["quantidade"] = df["quantidade"].fillna(1).astype(int)

    # Cálculo da coluna de Valor Total
    df["valor_total"] = df["valor_unitario"] * df["quantidade"]

    # Adiciona data de processamento
    df["data_processamento"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return df

# 3. Carga de Dados no Banco SQL
def salvar_no_banco_sql(df):
    db_name = "empresa_vendas.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Criação da tabela via instrução DDL
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas_processadas (
        id_venda INTEGER PRIMARY KEY,
        cliente TEXT NOT NULL,
        produto TEXT NOT NULL,
        valor_unitario REAL,
        quantidade INTEGER,
        valor_total REAL,
        data_venda TEXT,
        data_processamento TEXT
    )
    """)

    # Inserção dos dados limpos na tabela SQL
    df.to_sql("vendas_processadas", conn, if_exists="append", index=False)
    
    conn.commit()
    print(f"✓ Dados inseridos com sucesso no banco SQL '{db_name}'!")
    
    # Consulta SQL de validação
    print("\n📊 Resumo dos Dados no Banco de Dados (Consulta SQL):")
    resultado = cursor.execute("SELECT produto, SUM(valor_total) as total FROM vendas_processadas GROUP BY produto").fetchall()
    for linha in resultado:
        print(f"  • Produto: {linha[0]} | Faturamento Total: R$ {linha[1]:.2f}")

    conn.close()

if __name__ == "__main__":
    if not os.path.exists("vendas_brutas.csv"):
        gerar_dados_exemplo()
    
    dados_limpos = processar_dados()
    salvar_no_banco_sql(dados_limpos)