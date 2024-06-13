from fastapi import FastAPI, Request
from scripts.python_scripts.node_list import nodes
import requests
import json
import logging

app = FastAPI()

# Logger settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='./tig-stack/alloy/logs/fastapi.log', filemode='a')

@app.post("/receive_request")
async def receive_request(request: Request):
    data = await request.json()

    try:
        with open('scripts/data_json/efficient_node.json', 'r') as file:
            efficient_node = json.load(file)

        response = requests.post(str(efficient_node["url"]), json=data)
        logging.info(f'Request successfuly redirected to {efficient_node["name"]} node')

        if response.status_code != 200:
            logging.warning(f'Response not succed. HTTP status code: {response.status_code}')

        return response.json()
    except Exception as e:
        logging.error(f'Error sending JSON-RPC request: {str(e)}')
        return {"error": str(e)}