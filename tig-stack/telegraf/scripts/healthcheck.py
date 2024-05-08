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

            if response.status_code == 200:
                status = "online"
                response_time = t_fin - t_init
            else:
                status = "offline"
                response_time = None
        except Exception:
            status = "offline"
            response_time = None

        healthcheck.append({
            "name": node['name'],
            "status": status,
            "response_time": response_time
        })

    with open('healthcheck.json', 'w') as file:
        json.dump(healthcheck, file)

    return healthcheck



def select_node(healthcheck):
    # Search only for active nodes
    active_nodes = [healthcheck for result in healthcheck if result['status'] == 200]
    
    if not active_nodes:
        # If any node is active, return None
        node = None
    else:
        # Search the one with less time response
        node = min(healthcheck, key=lambda x:x['response_time'])

    # Save the efficient node in a JSON doc
    with open('efficient_node.json', 'w') as file:
        json.dump(node, file)


if __name__ == "__main__":
    # healthcheck_list = healthcheck()
    # select_node(healthcheck_list)
    print( json.dumps(healthcheck()) )
