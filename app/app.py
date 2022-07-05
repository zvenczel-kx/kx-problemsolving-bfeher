from flask import Flask
from random import randint
import os

app = Flask(__name__)

i, j = 2, 9

inmemorydict = {
  "nodename" : os.environ['APP'],  
  "size": randint(i, j),
  "iops": randint(i, j)
}

@app.route('/')
def sample():
    return inmemorydict

@app.route('/healthcheck')
def healthcheck():
    return "OK"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
