import pandas as pd
import os

# Verifica se o arquivo da planilha existe
if "ordem_de_compra.xlsx" in os.listdir():
    # Carregar a planilha Excel
    df_ordens = pd.read_excel("ordem_de_compra.xlsx")
else:
    # Cria um DataFrame vazio com as colunas mencionadas
    columns = [
        "CÓD. PEÇA", "MATERIAL", "ÁREA TOTAL", "ÁREA SUPERFICIAL", 
        "TEMPO DE CORTE", "DOBRAS", "REBITES", "ROSCAS", "SOLDA", 
        "QUANTIDADE", "LARGURA", "COMPRIMENTO", "HORAS LASER", 
        "HORAS REBITE", "HORAS DOBRADEIRA", "VALOR LASER", 
        "VALOR DOBRA", 'VALOR ROSCA', 'VALOR SOLDA', "VALOR REBITE", "VALOR MATERIAL", "QTD CHAPAS"
    ]
    df_ordens = pd.DataFrame(columns=columns)
    # Salva o DataFrame vazio como um arquivo Excel
    df_ordens.to_excel("ordem_de_compra.xlsx", index=False)

# Exemplo de como você pode limpar ou tratar os dados
df_ordens.fillna(0, inplace=True)

