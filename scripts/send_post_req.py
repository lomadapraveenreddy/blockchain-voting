import requests
import sys

URL = 'http://localhost:5000'

requests.post(f'{URL}/wallet/transact',json={
    "pollID":sys.argv[1],
    "option":sys.argv[2]
})