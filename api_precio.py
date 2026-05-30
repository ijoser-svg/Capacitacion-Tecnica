import requests

def obtener_precio_bitcoin():
    # URL de la API pública de CoinGecko
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    try:
        print("Consultando el precio actual de Bitcoin...")
        # Hacer la petición a la API
        respuesta = requests.get(url)
        
        # Verificar si la conexión fue exitosa (Código 200)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            # Extraer el precio del JSON recibido
            precio_usd = datos['bitcoin']['usd']
            print("\n======================================")
            print(f"💰 El precio actual de Bitcoin es: ${precio_usd:,} USD")
            print("======================================\n")
        else:
            print(f"Error al conectar con la API. Código de estado: {respuesta.status_code}")
            
    except Exception as e:
        print(f"Ocurrió un error de red: {e}")

if __name__ == "__main__":
    obtener_precio_bitcoin()