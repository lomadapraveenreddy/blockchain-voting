import uuid
import time
import config
from wallet.wallet import Wallet
class Transaction:
    """
    This has the data of the votes.
    """
    def __init__(self,senderWallet,pollID,option):
        self.transactionID = str(uuid.uuid4())[:8]
        self.output=self.createOutput(pollID=pollID,option=option)
        self.input = self.createInput(wallet=senderWallet,output=self.output)
    
    def createOutput(self,pollID,option):
        output={}
        output[pollID]={'option':option}
        return output
    
    def createInput(self,wallet,output):
        
        return {
            'timestamp': time.time_ns(),
            'senderAddress': wallet.address,
            'publicKey': wallet.public_key,
            'signature': wallet.sign(output),
        }
    
    def toJson(self):

        return self.__dict__

    @staticmethod
    def isValidTransaction(transaction):
        '''
        validates and raises an exception if invalid.
        '''

        if not Wallet.verify(transaction.input['publicKey'], transaction.output, transaction.input['signature']):
            raise Exception('Invalid signature')

def main():
    transaction= Transaction(Wallet(),'receip','1')
    try:
        print(Transaction.isValidTransaction(transaction))
    except Exception as e:
        print(f'exception {e}')

if __name__ == '__main__':
    main()