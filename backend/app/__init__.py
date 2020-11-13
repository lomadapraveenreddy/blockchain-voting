import os
import random
import requests
from flask import Flask,jsonify,request,render_template
from blockchain.blockchain import Blockchain
# from backend.app.src import blockchain
from wallet.wallet import Wallet
from wallet.transaction import Transaction
from wallet.transaction_pool import TransactionPool
from backend.pubsub import PubSub
app = Flask(__name__,template_folder='src')

blockchain =Blockchain()
wallet = Wallet()
transactionPool = TransactionPool()
pubsub = PubSub(blockchain,transactionPool)

@app.route('/')
def routeDefault():
    return 'Welcome'

@app.route('/blockchain')
def routeBlockchain():
    # return jsonify(blockchain.toJson())
    return render_template("blockchain.html",ledger=blockchain.ledger)

@app.route('/blockchain/mine')
def routeBlockchainMine():
    data='foo'
    transactionValues = transactionPool.transactionMap.values()
    data = list(
        map(lambda transaction: transaction.toJson(),transactionValues)
    )
    blockchain.addBlock(data)
    blockMined=blockchain.ledger[-1]
    pubsub.broadcastBlock(blockMined)
    return jsonify(blockMined.toJson())

@app.route('/wallet/transact',methods=['POST'])
def route_Wallet_Transact():
    transactionData=request.get_json()
    # transaction= transactionPool.existingTransaction(wallet.address) 
    # if transaction:
    transaction=Transaction(wallet,transactionData['pollID'],transactionData['option'])
    pubsub.broadcastTransaction(transaction)
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