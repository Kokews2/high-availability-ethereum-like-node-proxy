import requests
import time
import json
from node_list import nodes    

def healthcheck():
    # Build the request
    rpc_payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }

    # Measurements
    response_times = {}
    status_codes  = {}
    block_numbers = {}

    healthcheck = []

    less_response_time = 10
    efficient_node = nodes[0]

    # HEALTHCHECK ALGORITHM
    for node in nodes:
        url = node['url']
        try:
            t_init = time.time()
            response = requests.post(url, json=rpc_payload)
            t_fin = time.time()

            # Status code
            status_codes[node['name']] = response.status_code
            if response.status_code == 200:
                # Response time
                response_times[node['name']] = t_fin - t_init
                
                # Last block number
                block_numbers[node['name']] = int(response.json()["result"], 16)

                # Efficient node
                if (t_fin-t_init) < less_response_time:
                    less_response_time = t_fin - t_init
                    efficient_node = node
            else:
                response_times[node['name']] = None
                block_numbers[node['name']] = None
        except Exception:
            status_codes[node['name']] = -1
            response_times[node['name']] = None
            block_numbers[node['name']] = None

    healthcheck.append({
        "measurement": "status_code",
        **status_codes
    })

    healthcheck.append({
        "measurement": "response_time",
        **response_times
    })

    healthcheck.append({
        "measurement": "block_number",
        **block_numbers
    })

    # SAVING THE DATA IN JSON FILES
    with open('/opt/scripts/data_json/healthcheck.json', 'w') as file:
        json.dump(healthcheck, file)

    with open('/opt/scripts/data_json/efficient_node.json', 'w') as file:
        json.dump(efficient_node, file)

    return healthcheck

"""
    # SELECT EFFICIENT NODE
    active_nodes = [node for node in healthcheck if node['status'] == 200]
    
    if active_nodes:
        efficient_node = min(active_nodes, key = lambda x : x['response_time'])
    else:
        efficient_node = None
"""
    

if __name__ == "__main__":
    print( json.dumps(healthcheck()) )
