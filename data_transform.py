import pandas as pd

# Ruta del archivo CSV intermedio
archivo_csv = 'clientes.csv'

try:
    # Leer el archivo CSV
    data = pd.read_csv(archivo_csv)
    
    # REGLA_1: Ordenar los datos por nombre
    data_ordenada = data.sort_values(by='Nombre1')
    
    # REGLA_2: 2
    
    # REGLA_3: 3
    
    # REGLA_4: 4
    
    
    # Exportar a Excel
    archivo_excel = 'clientes_ordenados.xlsx'
    data_ordenada.to_excel(archivo_excel, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")