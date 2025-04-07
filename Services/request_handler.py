import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()


class Request:
    def __init__(self, url=os.getenv("REQUEST_URL"), path=''):
        self.url = url
        self.path = path
        self.headers = {'Accept': '*/*', 'Content-Type': 'application/json'}
        self.method = {
            'GET': requests.get, 
            'POST': requests.post, 
            'DELETE': requests.delete, 
            'PATCH': requests.patch
        }

        self.response = 0


    def send_request(self, method: str, path: str, payload: str = '') -> requests.Response:
        full_url = self.url + path
        params = {'url': full_url, 'headers': self.headers, 'data': payload}
        self.response = self.method[method](**params)
        return self.response