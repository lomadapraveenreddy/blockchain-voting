import requests

URL = 'http://localhost:5000'

requests.post(f'{URL}/wallet/transact',json={
    "pollID":"123",
    "option":"asd"
}).json()