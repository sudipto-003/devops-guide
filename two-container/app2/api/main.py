from flask import Flask
import time
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

app = Flask(__name__)

@app.route('/')
def getFromNode():
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http', adapter)

    wel = session.get('http://nodeexp:8080').text
    data = time.time()

    return {'node': wel, 'python': data}