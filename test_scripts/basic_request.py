import requests

def get_latest_block_number(node_url):
    # Construir el cuerpo de la solicitud JSON-RPC
    rpc_payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1  # Identificador de la solicitud, puede ser cualquier valor
    }

    try:
        # Enviar la solicitud HTTP POST al nodo Ethereum
        response = requests.post(node_url, json=rpc_payload)
        # Leer la respuesta JSON
        data = response.json()
        # Imprimir toda la respuesta
        print(data)
        # Verificar si la respuesta contiene el número de bloque
        if "result" in data:
            block_number_hex = data["result"]
            # Convertir el número de bloque hexadecimal a decimal
            block_number = int(block_number_hex, 16)
            return block_number
        else:
            print("Error: No se pudo obtener el número de bloque.")
    except Exception as e:
        print("Error al enviar la solicitud JSON-RPC:", e)

# URL del nodo Ethereum JSON-RPC
node_url = "https://ethereum-rpc.publicnode.com"

# Obtener el número de bloque más reciente
latest_block_number = get_latest_block_number(node_url)
print("Número de bloque más reciente:", latest_block_number)
