import pandas as pd
def calculate_peso(material_type):
    data = {
        "Peso": ["12.717", "25.434", "35.325", "43.803", "55.107", "74.889", "86.193","12.717", "25.434", "33.912", "42.390", "53.694", "74.889", 
            "84.780", "134.235", "179.451", "226.080", "268.470", "358.902", "188.400", "298.300"],
        "Material": [
            "CHAPA DE ACO GALVANIZADO #26 0.45X1200X3000",
            "CHAPA DE ACO GALVANIZADO #20 0.9X1200X3000",
            "CHAPA DE ACO GALVANIZADO #18 1.25X1200X3000",
            "CHAPA DE ACO GALVANIZADO #16 1.55X1200X3000",
            "CHAPA DE ACO GALVANIZADO #14 1.95X1200X3000",
            "CHAPA DE ACO GALVANIZADO #12 2.65X1200X3000",
            "CHAPA DE ACO GALVANIZADO #11 3.05X1200X3000",
            "CHAPA ACO CARBONO #26 0.45X1200X3000",
            "CHAPA ACO CARBONO #20 0.90X1200X3000",
            "CHAPA ACO CARBONO #18 1.20X1200X3000",
            "CHAPA ACO CARBONO #16 1.50X1200X3000",
            "CHAPA ACO CARBONO #14 1.9X1200X3000",
            "CHAPA ACO CARBONO #12 2.65X1200X3000",
            "CHAPA ACO CARBONO #1-8 3.0X1200X3000",
            "CHAPA ACO CARBONO #3-16 4.75X1200X3000",
            "CHAPA ACO CARBONO #1-4 6.35X1200X3000",
            "CHAPA ACO CARBONO #5-16 8X1200X3000",
            "CHAPA ACO CARBONO #3-8 9.5X1200X3000",
            "CHAPA ACO CARBONO #1-2 12.7X1200X3000",
            "CHAPA ACO CARBONO #1020 GR 5-8 16X1000X1500",
            "CHAPA ACO CARBONO #1020 GR 3-4 19X1000X2000"
        ]  
        
    }
    
    df = pd.DataFrame(data)
    
    if not isinstance(material_type, str):
        material_type = str(material_type)
    
    resultado = df[df['Material'].str.contains(material_type, case=False)]
    
    if not resultado.empty:
        return resultado['Peso'].values[0]
    else:
        return 0  # Retorna 0 caso não encontre o material