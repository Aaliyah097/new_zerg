import requests
import json


class Bitconce:
    def __init__(self, token: str):
        self.base_url = "https://bitconce.top/api/"
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }
        self.session = requests.Session()
        self.session.headers = self.headers

    def request(self, url: str, method: str, payload: dict = None, params: dict = None) -> dict:
        if params:
            url += "?"
            for key, value in params.items():
                url += f"{key}={value}&"

        response = self.session.request(
            method=method,
            url=self.base_url + url,
            data=payload if payload else {}
        )
        if response.status_code in [200, 201]:
            response = json.loads(response.text)
            if response['status'] == 'Error':
                raise Exception(response['description'])
            if 'data' in response:
                return response['data']
            elif 'orders' in response:
                return response['orders']
            elif 'order' in response:
                return response['order']
            elif 'wallets' in response:
                return response['wallets']
            else:
                return response
        else:
            raise Exception(response.text)
