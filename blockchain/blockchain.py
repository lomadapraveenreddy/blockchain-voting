from block import Block
import time
from hashlib import sha256
class Blockchain:
    """
    This is the blockchain ledger class.
    This stores the complete ledger. 
    """
    
    def addBlock(self,data):
        """
        this method adds a block to the ledger having the data.
        data is usually the list of votes casted.
        """
        self.ledger.append(Block.mineBlock(self.ledger[-1],data))

    def __init__(self):
        self.ledger =[Block.genesisBlock()]
        


    def __repr__(self):
        return f'Ledger -\n {self.ledger}'


if __name__ == '__main__':
    blockchain = Blockchain()
    blockchain.addBlock(data='1')
    blockchain.addBlock(data='2')
    print(blockchain)