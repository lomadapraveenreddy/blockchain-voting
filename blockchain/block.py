import time
from utils.crypto import sha256Hash
from blockchain.vote import Vote
from .config import MINE_RATE
GENESIS_DATA ={
    'timestamp': 1,
    'data': [],
    'hash': 'genesisHash',
    'previousHash':'',
    'difficulty':4,
    'nonce': 'genesisNonce'
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
        nonce=0
        timestamp=time.time_ns()
        difficulty=Block.getDifficulty(lastBlock,timestamp)
        blockHash= sha256Hash(timestamp,data,lastBlock.hash,difficulty,nonce)
        while blockHash[0:difficulty]!='0'*difficulty:
            nonce=nonce+1
            timestamp=time.time_ns()
            difficulty=Block.getDifficulty(lastBlock,timestamp)
            blockHash= sha256Hash(timestamp,data,lastBlock.hash,difficulty,nonce)
        return Block(timestamp=timestamp,data=data,hash=blockHash,previousHash=lastBlock.hash,difficulty=difficulty,nonce=nonce)
            

    def __init__(self,timestamp,data,hash,previousHash,difficulty,nonce):
        self.timestamp=timestamp
        self.data=data
        self.hash=hash
        self.previousHash=previousHash
        self.difficulty=difficulty
        self.nonce=nonce

    def __repr__(self):
        return (f'( Block- '
            f'timestamp: {self.timestamp}, '
            f'data: {self.data}, '
            f'hash: {self.hash}, '
            f'previousHash: {self.previousHash}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce})\n'
            )

    @staticmethod
    def getDifficulty(lastBlock,timestamp):
        """
        Returns the difficulty of the new block.
        """
        if timestamp-lastBlock.timestamp<MINE_RATE:
            return lastBlock.difficulty+1
        
        if lastBlock.difficulty-1>0:
            return lastBlock.difficulty-1
        return 1

if __name__ == '__main__':
    print(Block.genesisBlock())
    print(Block.mineBlock(lastBlock=Block.genesisBlock(),data=[Vote('1','2').__dict__]))
    
    
    
