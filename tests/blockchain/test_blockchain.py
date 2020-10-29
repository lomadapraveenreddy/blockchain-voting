from blockchain.blockchain import Blockchain
from blockchain.block import GENESIS_DATA

def test_blockchain_instance():
    blockchain=Blockchain()

    assert blockchain.ledger[0].hash==GENESIS_DATA['hash']

def test_add_block():
    blockchain=Blockchain()
    data='test-data'
    blockchain.addBlock(data)

    assert blockchain.ledger[-1].data==data