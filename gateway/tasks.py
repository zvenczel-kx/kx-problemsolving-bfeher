import random
def healthcheck(register):
    for server in register:
        server.healthcheck_and_update_status()
    return register

def get_healthy_server(register):
    try:
        return random.choice([server for server in register if server.healthy])
    except IndexError:
        return None
