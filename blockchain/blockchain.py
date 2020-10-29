from blockchain.block import Block
from blockchain.vote import Vote
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
    # blockchain = Blockchain()
    # blockchain.addBlock(data=[Vote('1','a'),Vote('1','b')])
    # blockchain.addBlock(data=[Vote('1','b'),Vote('1','a')])
    # print(blockchain)
    print(Vote('1','2').__dict__)