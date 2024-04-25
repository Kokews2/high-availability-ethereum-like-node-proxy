import requests
import time
import json
from node_list import nodes

def healthcheck():
    # Build the request
    rpc_payload = {
        "jsonrpc": "2.0",
        "method": "web3_clientVersion",
        "params": [],
        "id": 1 
    }

    healthcheck = []

    for node in nodes:
        try:
            # Get the node URL
            url = node['url']

            t_init = time.time()
            response = requests.post(url, json=rpc_payload)
            t_fin = time.time()

            result = {
                "name": node['name'],
                "url": node['url'],
                "status": response.status_code,
                "response_time": t_fin - t_init
            }
            
        except Exception as e:
            # status=1 (ERROR)
            result = {
                "name": node['name'],
                "url": node['url'],
                "status": 1,
                "response_time": None
            }   

        healthcheck.append(result)

        # Safe the healthcheck results in a JSON file
        with open('healthcheck_results.json', 'w') as file:
            json.dump(healthcheck, file)

    return healthcheck



def select_node():
    # Obtain the healthcheck list
    healthcheck_list = healthcheck()

    # Search only for active nodes
    active_nodes = [healthcheck_list for result in healthcheck_list if result['status'] == 200]
    
    if not active_nodes:
        # If any node is active, return None
        node = None
    else:
        # Search the one with less time response
        node = min(healthcheck_list, key=lambda x:x['response_time'])

    # Save the efficient node in a JSON doc
    with open('efficient_node.json', 'w') as file:
        json.dump(node, file)


if __name__ == "__main__":
    select_node()

"""
if __name__ == "__main__":
    healthcheck = healthcheck()
    print("Resultados del healthcheck:")
    for result in healthcheck:
        print(f"Nodo: {result['name']}, Estado: {result['status']}, Tiempo Respuesta: {result['response_time']}")

    node = select_node(healthcheck)
    print("\nNodo más eficiente:")
    print(f"Nodo: {node['name']}, Estado: {node['status']}, Tiempo Respuesta: {node['response_time']}")
"""
