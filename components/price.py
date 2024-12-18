import pandas as pd
from components.data_material import calculate_peso
import os
import shutil

class Pricer():
    
    def __init__(self, sheets):
        self.data = sheets
        self.custo_laser_s = 0.1515
        self.custo_dobra_min = 13.33
        self.custo_rebite_30s = 2.272
        self.custo_rosca_min = 3.41
        self.custo_solda_min = 0.1515
        self.custo_pintura = 60
        self.new_data = ' '
        self.calculate_price()
        
        
    def clean_all(self):
            if os.path.exists(self.data):
                shutil.rmtree(self.data)    
                
    def calculate_price(self):
        # Ler os dados do arquivo Excel
        df = pd.read_excel(self.data)
        
        # Colunas de dados e resultados
        data_columns = ["CÓD. PEÇA", "MATERIAL", "ÁREA TOTAL", "TEMPO DE CORTE", "DOBRAS", "REBITES", "ROSCAS", "SOLDA", "QUANTIDADE", "LARGURA", "COMPRIMENTO"]
        
        # Verificar se todas as colunas necessárias existem no DataFrame
        colunas_existentes = [col for col in data_columns if col in df.columns]
        colunas_ausentes = set(data_columns) - set(colunas_existentes)

        if colunas_ausentes:
            print(f"As seguintes colunas não foram encontradas na planilha: {colunas_ausentes}")
            return

        print("Todas as colunas especificadas foram encontradas na planilha.")

        # Criar um novo DataFrame com as colunas selecionadas
        new_df = df[colunas_existentes].copy()

        # Função auxiliar para converter valores em float
        def to_float(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return 0.0

        # Converter colunas relevantes para float
        for coluna in ["TEMPO DE CORTE", "DOBRAS", "REBITES", "ROSCAS", "SOLDA", "QUANTIDADE", "LARGURA", "COMPRIMENTO"]:
            if coluna in new_df.columns:
                new_df[coluna] = new_df[coluna].apply(to_float)

        # Funções específicas para cada coluna de resultados
        def calcular_total_chapas(row):
            
            largura = row["LARGURA"]
            comprimento = row["COMPRIMENTO"]
            quantidade = row["QUANTIDADE"]
            # Dimensões da chapa padrão
            chapa_largura = 1150  # em mm
            chapa_comprimento = 2950  # em mm
            
            # Calcular a área de uma chapa
            area_chapa = chapa_largura * chapa_comprimento  # em mm²
            
            # Calcular a área total das chapas necessárias
            area_total = largura * comprimento * quantidade  # em mm²
            
            # Calcular a quantidade de chapas necessárias
            chapas_necessarias = (area_total / area_chapa)
    
            return chapas_necessarias
            
        def calcular_valor_material(row):
            try:
            # Garantir que 'ÁREA TOTAL' e 'QUANTIDADE' sejam convertidos para números (float)
                material_total = float(row["ÁREA TOTAL"]) * float(row["QUANTIDADE"])
            except ValueError:
            # Caso ocorra um erro de conversão, você pode definir material_total como 0 ou outro valor padrão
                material_total = 0
                print(f"Erro na conversão de dados para linha: {row}")
            
            # Obtém o tipo do material
            material_type = row["MATERIAL"]
            
            # Calcula o peso usando a função calculate_peso
            peso = float(calculate_peso(material_type))
            
            # Definição do valor de chapa por metro quadrado
            chapa_m2 = 3.6
            
            # Calcula o valor
            valor = ((material_total * peso) / chapa_m2) * 10
            return valor
            
        def calcular_valor_laser(row):
            return row["TEMPO DE CORTE"] * row["QUANTIDADE"] * self.custo_laser_s

        def calcular_valor_dobras(row):
            return row["DOBRAS"] * row["QUANTIDADE"] * self.custo_dobra_min

        def calcular_valor_rebite(row):
            return row["REBITES"] * row["QUANTIDADE"] * self.custo_rebite_30s

        def calcular_valor_rosca(row):
            return row["ROSCAS"] * row["QUANTIDADE"] * self.custo_rosca_min

        def calcular_valor_solda(row):
            return row["SOLDA"] * row["QUANTIDADE"] * self.custo_solda_min


        def get_data(row):
            
            data = "20/12/2024"
            return data
        
        def calcular_hora_rebite(row):
            return row["REBITES"] * (1/120)
        
        def calcular_hora_dobradeira(row):
            return row["DOBRAS"] * (1/10)
        
        def calcular_hora_laser(row):
            return row["TEMPO DE CORTE"]/3600
        
        
        
        # Mapeamento das colunas de resultados para suas funções
        funcoes_resultados = {
            "VALOR MATERIAL": calcular_valor_material,
            "VALOR LASER": calcular_valor_laser,
            "VALOR DOBRA": calcular_valor_dobras,
            "VALOR REBITE": calcular_valor_rebite,
            "VALOR ROSCA": calcular_valor_rosca,
            "VALOR SOLDA": calcular_valor_solda,
            "QTD CHAPAS": calcular_total_chapas,
            "HORAS REBITE": calcular_hora_rebite,
            "HORAS DOBRADEIRA": calcular_hora_dobradeira,
            "HORAS LASER": calcular_hora_laser,
            "DATA": get_data,
        }

        # Aplicar as funções específicas para cada coluna de resultados
        for resultado, funcao in funcoes_resultados.items():
            new_df[resultado] = new_df.apply(funcao, axis=1)

        
        # Salvar a nova planilha com os resultados
        
        file_name = "ordem_de_compra.xlsx"

        # Verifica se o arquivo já existe
        if os.path.exists(file_name):
            os.remove(file_name)  # Apaga o arquivo existente

        # Salva a nova planilha
        new_df.to_excel(file_name, index=False)

    
    def move_sheet(self):
        pass


