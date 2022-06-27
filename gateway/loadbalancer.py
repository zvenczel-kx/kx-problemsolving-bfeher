from http import server
from turtle import up
from flask import Flask, request, jsonify
import requests, random
from tasks import healthcheck, get_healthy_server
from models import Server
import sys
import os
import json

loadbalancer = Flask(__name__)
config = os.environ.get("CONFIG").split(" ")
register = [Server(server) for server in config]

@loadbalancer.route("/")
@loadbalancer.route("/<path>")
def router(path="/"):
    updated_register = healthcheck(register)
    healthy_server = get_healthy_server(updated_register)
    if not healthy_server:
        return "No Backends servers available", 503
    if ("/" + path) == "/data":
        response = requests.get("http://{}".format(healthy_server.endpoint))
        return response.json()
    if ("/" + path) == "/status":
        response = loadbalancer.response_class(
            response=json.dumps(updated_register, default=lambda updated_register: updated_register.__dict__),
            status=200,
            mimetype='application/json'
        )   
        return response
    
    return "Not Found", 404

if __name__ == '__main__':
    loadbalancer.run(host="0.0.0.0", debug=True)
