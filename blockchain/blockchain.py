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

    def replaceLedger(self, ledger):
        '''
        replace local ledger with incoming chains
        '''
        if len(ledger) <= len(self.ledger):
            raise Exception('cannot replace. The incoming chain must be longer.')

        try:
            Blockchain.isValidLedger(ledger)
        except Exception as e:
            raise Exception(f'cannot replace. The incoming chain is invalid: {e}')

        self.ledger = ledger

    @staticmethod
    def isValidLedger(ledger):
        '''
        validate the ledger
        '''
        if ledger[0]!=Block.genesisBlock():
            raise Exception('genesis block must be valid')

        for i in range(1,len(ledger)):
           block = ledger[i]
           lastBlock = ledger[i-1]
           Block.isValidBlock(lastBlock, block)

    @staticmethod
    def fromJson(jsonChain):

        blockchain=Blockchain()
        blockchain.ledger=list(map(lambda jsonBlock: Block.fromJson(jsonBlock),jsonChain))
        return blockchain

    def toJson(self):
        '''
        Serializing the blockchain class.
        '''
        jsonLedger = []

        for block in self.ledger:
            jsonLedger.append(block.toJson())
        
        return jsonLedger

if __name__ == '__main__':
    blockchain = Blockchain()
    blockchain.addBlock(data=[Vote('1','b').__dict__,Vote('1','a').__dict__])
    blockchain.addBlock(data=[Vote('1','b').__dict__,Vote('1','a').__dict__])
    blockchain.addBlock(data=[Vote('1','b').__dict__,Vote('1','a').__dict__])
    print(blockchain)
    