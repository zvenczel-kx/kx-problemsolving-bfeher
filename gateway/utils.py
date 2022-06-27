from models import Server
import random

def get_healthy_server(host, register):
    try:
        return random.choice([server for server in register[host] if server.healthy])
    except IndexError:
        return None
