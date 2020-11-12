import os
import random
import requests
from flask import Flask,jsonify,request
from blockchain.blockchain import Blockchain
from wallet.wallet import Wallet
from wallet.transaction import Transaction
from backend.pubsub import PubSub
app = Flask(__name__)

blockchain =Blockchain()
wallet = Wallet()
pubsub = PubSub(blockchain)

@app.route('/')
def routeDefault():
    return 'Welcome'

@app.route('/blockchain')
def routeBlockchain():
    return jsonify(blockchain.toJson())

@app.route('/blockchain/mine')
def routeBlockchainMine():
    data='foo'
    blockchain.addBlock(data)
    blockMined=blockchain.ledger[-1]
    pubsub.broadcastBlock(blockMined)
    return jsonify(blockMined.toJson())

@app.route('/wallet/transact',methods=['POST'])
def route_Wallet_Transact():
    transactionData=request.get_json()
    transaction= Transaction(wallet,transactionData['pollID'],transactionData['option'])
    return jsonify(transaction.toJson())
    




ROOT_PORT=5000
PORT = ROOT_PORT
if os.environ.get('PEER')=='True':
    PORT = random.randint(5001,6000)
    result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
    ledgerFromOtherNodes= (Blockchain.fromJson(result.json())).ledger
    try:
        blockchain.replaceLedger(ledgerFromOtherNodes)
    except Exception as e:
        print(f'exception in synchronising ledger {e}.')
print(PORT)
app.run(port=PORT)