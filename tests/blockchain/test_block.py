from blockchain.block import Block,GENESIS_DATA
import time
import pytest

def test_genesisBlock(): # testing genesis block
    block = Block(**GENESIS_DATA)
    assert isinstance(block,Block)
    assert block.timestamp==GENESIS_DATA['timestamp']
    assert block.data==GENESIS_DATA['data']
    assert block.hash==GENESIS_DATA['hash']
    assert block.previousHash==GENESIS_DATA['previousHash']
    


def test_mineBlock(): # testing mine block
    data ='test'
    block = Block.mineBlock(Block.genesisBlock(),data)
    assert isinstance(block, Block)
    assert block.previousHash==GENESIS_DATA['hash'] 
    assert block.data==data
    assert block.hash[0:block.difficulty]=='0'*block.difficulty 
@pytest.fixture
def lastBlock():
    return Block.genesisBlock()

@pytest.fixture
def block (lastBlock):
    return Block.mineBlock(lastBlock, 'test')

def test_isValidBlock(lastBlock, block):
    Block.isValidBlock(lastBlock, block)

def test_isValidBlockBadLastHash(lastBlock, block):
    block.previousHash = 'bad_hash'

    with pytest.raises(Exception,match='previous hash of this block\
                 does not match with hash of previous block'):
        Block.isValidBlock(lastBlock, block)
    
def test_isValidBlockBadProofOfWork(lastBlock, block):
    block.hash = 'bad_hash'

    with pytest.raises(Exception,match='Proof of work mismatch'):
        Block.isValidBlock(lastBlock, block)

def test_isValidBlockJumpDifficulty(lastBlock, block):
    jump_difficulty = 10
    block.difficulty = jump_difficulty
    block.__hash__ = f'{"0" * jump_difficulty}111abbc'

    with pytest.raises(Exception,match='difficulty change is more than 1'):
         Block.isValidBlock(lastBlock, block)

def test_isValidBlockBadHash(lastBlock, block):
    block.hash = '0000000000000000000000000bbabc'

    with pytest.raises(Exception,match='Hash does not match'):
         Block.isValidBlock(lastBlock, block)

