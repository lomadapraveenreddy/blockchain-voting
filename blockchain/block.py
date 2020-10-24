import time
from utils.crypto import sha256Hash
from blockchain.vote import Vote
GENESIS_DATA ={
    'timestamp': 1,
    'data': [],
    'hash': 'genesisHash',
    'previousHash':''
}
class Block:
    """
    This is a block class which stores the information
    of the votes casted by the user.
    """

    @staticmethod
    def genesisBlock():
        return Block(**GENESIS_DATA)
    
    @staticmethod
    def mineBlock(lastBlock,data):
        """
        this method mines the new block 
        """
        timestamp=time.time_ns()
        blockHash= sha256Hash(timestamp,data,lastBlock.hash)
        return Block(timestamp=timestamp,data=data,hash=blockHash,previousHash=lastBlock.hash)

    def __init__(self,timestamp,data,hash,previousHash):
        self.timestamp=timestamp
        self.data=data
        self.hash=hash
        self.previousHash=previousHash

    def __repr__(self):
        return (f'( Block- '
            f'timestamp: {self.timestamp}, '
            f'data: {self.data}, '
            f'hash: {self.hash}, '
            f'previousHash: {self.previousHash})\n'
            )


if __name__ == '__main__':
    block = Block('1','2','3','4')
    print(block)
    print(Block.genesisBlock())
    print(Block.mineBlock(lastBlock=block,data=[Vote('1','2').__dict__]))
    
    
