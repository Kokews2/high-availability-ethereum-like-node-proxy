from fastapi import FastAPI, Request
from nodes.node_list import nodes
import requests
import json

app = FastAPI()

@app.post("/receive_request")
async def receive_request(request: Request):
    data = await request.json()

    try:
        with open('nodes/results.json', 'r') as file:
            efficient_node = json.load(file)            

        response = requests.post(str(efficient_node["url"]), json=data)
        return response.json()
    except Exception as e:
        print(efficient_node)
        print("Error sending JSON-RPC request:", e)