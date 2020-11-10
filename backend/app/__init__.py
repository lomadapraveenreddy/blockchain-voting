import os
import random
from flask import Flask,jsonify
from blockchain.blockchain import Blockchain
from backend.pubsub import PubSub
app = Flask(__name__)

blockchain =Blockchain()
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

PORT = 5000
if os.environ.get('PEER')=='True':
    PORT = random.randint(5001,6000)
print(PORT)
app.run(port=PORT)