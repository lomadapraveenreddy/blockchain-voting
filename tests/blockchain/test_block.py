from blockchain.block import Block,GENESIS_DATA

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
