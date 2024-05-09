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

    # HEALTHCHECK ALGORITHM
    for node in nodes:
        url = node['url']
        try:
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
            "url": url,
            "status": status,
            "response_time": response_time
        })


    # SELECT EFFICIENT NODE
    active_nodes = [node for node in healthcheck if node['status'] == "online"]
    
    if healthcheck:
        efficient_node = min(active_nodes, key = lambda x : x['response_time'])
    else:
        efficient_node = None


    # SAVING THE DATA IN JSON FILES
    with open('/opt/scripts/data_json/healthcheck.json', 'w') as file:
        json.dump(healthcheck, file)

    with open('/opt/scripts/data_json/efficient_node.json', 'w') as file:
        json.dump(efficient_node, file)

    return healthcheck

if __name__ == "__main__":
    print( json.dumps(healthcheck()) )
