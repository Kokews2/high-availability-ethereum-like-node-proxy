from fastapi import FastAPI, Request
from scripts.python_scripts.node_list import nodes
import requests
import json
import logging
from colorama import init, Fore, Style

app = FastAPI()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
init(autoreset=True) # colorama settings

@app.post("/receive_request")
async def receive_request(request: Request):
    data = await request.json()

    try:
        with open('scripts/data_json/efficient_node.json', 'r') as file:
            efficient_node = json.load(file)

        response = requests.post(str(efficient_node["url"]), json=data)
        logging.info(f'Request redirected to {Fore.GREEN}{efficient_node["name"]}{Style.RESET_ALL} node')

        if response.status_code != 200:
            logging.warning(f'Response not succed. HTTP status code: {Fore.RED}{response.status_code}{Style.RESET_ALL}')

        return response.json()
    except Exception as e:
        logging.error(f'Error sending JSON-RPC request: {Fore.RED}{e}{Style.RESET_ALL}')
        return {"error": str(e)}