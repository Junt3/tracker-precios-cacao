import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# Archivo donde se guardará el historial
ARCHIVO_HISTORIAL = "historial_precios_cacao.csv"

def obtener_precio_ice_ny():
    """
    Obtiene el precio de cierre más reciente de los futuros 
    de Cacao (CC=F) en ICE Nueva York usando Yahoo Finance.
    """
    try:
        # El ticker 'CC=F' corresponde a los futuros de Cocoa (Cacao)
        cacao_ticker = yf.Ticker("CC=F")
        datos = cacao_ticker.history(period="1d")
        
        if not datos.empty:
            # El precio viene en dólares por tonelada métrica
            precio_actual = datos['Close'].iloc[-1]
            return round(precio_actual, 2)
        else:
            return None
    except Exception as e:
        print(f"Error al conectar con el mercado internacional: {e}")
        return None

def registrar_precios(precio_internacional, precio_local):
    """
    Guarda los precios del día en un archivo CSV.
    """
    fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    nuevo_registro = pd.DataFrame([{
        "Fecha": fecha_hoy,
        "Precio_ICE_NY_USD_Ton": precio_internacional,
        "Precio_Local_Ecuador_Quintal": precio_local
    }])
    
    # Si el archivo ya existe, añade la fila; si no, crea el archivo con encabezados
    if os.path.exists(ARCHIVO_HISTORIAL):
        nuevo_registro.to_csv(ARCHIVO_HISTORIAL, mode='a', header=False, index=False)
    else:
        nuevo_registro.to_csv(ARCHIVO_HISTORIAL, mode='w', header=True, index=False)
        
    print(f"Precios registrados exitosamente el {fecha_hoy}")

def main():
    print("="*40)
    print("TRACKER AUTOMATIZADO DE PRECIOS DEL CACAO")
    print("="*40)
    
    print("\nObteniendo datos del mercado internacional (ICE Nueva York)...")
    precio_ny = obtener_precio_ice_ny()
    
    if precio_ny:
        print(f"Precio actual en Nueva York: ${precio_ny} / Tonelada")
    else:
        print("No se pudo recuperar el precio de Nueva York.")
        
    # El mercado local en Ecuador (SIPA u otras fuentes) suele requerir ingreso manual 
    # o web scraping específico. Aquí permitimos el ingreso para el registro.
    try:
        precio_ecuador = float(input("\nIngrese el precio de compra local actual (USD por Quintal): "))
    except ValueError:
        print("Entrada inválida. Se registrará como 0.0")
        precio_ecuador = 0.0
        
    registrar_precios(precio_ny, precio_ecuador)
    
    print("\nResumen guardado en:", ARCHIVO_HISTORIAL)
    print("="*40)

if __name__ == "__main__":
    main()