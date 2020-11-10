import pytest
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

@pytest.fixture
def blockchain_three_blocks():
    blockchain = Blockchain()
    for i in range(3):
        blockchain.addBlock(i)
    return blockchain


def test_isValidLedger(blockchain_three_blocks):
    Blockchain.isValidLedger(blockchain_three_blocks.ledger)

def test_isValidLedgerBadLedger(blockchain_three_blocks):
    blockchain_three_blocks.ledger[0].hash = 'bad_hash'

    with pytest.raises(Exception, match='genesis block must be valid'):
        Blockchain.isValidLedger(blockchain_three_blocks.ledger)

def test_replaceLedger(blockchain_three_blocks):
    blockchain = Blockchain()
    blockchain.replaceLedger(blockchain_three_blocks.ledger)

    assert blockchain.ledger == blockchain_three_blocks.ledger

def test_replaceLedgerNotLonger(blockchain_three_blocks):
    blockchain = Blockchain()

    with pytest.raises(Exception, match='cannot replace. The incoming chain must be longer.'):
        blockchain_three_blocks.replaceLedger(blockchain.ledger)

def test_replaceLedgerBadLedger(blockchain_three_blocks):
    blockchain = Blockchain()
    blockchain_three_blocks.ledger[1].hash = 'bad_hash'

    with pytest.raises(Exception, match='cannot replace. The incoming chain is invalid:'):
        blockchain.replaceLedger(blockchain_three_blocks.ledger)
