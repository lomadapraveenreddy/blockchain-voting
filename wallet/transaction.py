import uuid
import time
import config
from wallet.wallet import Wallet
class Transaction:
    """
    This has the data of the votes.
    """
    def __init__(self,senderWallet=None,pollID=None,option=None,transactionID=None,output=None,input=None):
        self.transactionID = transactionID or str(uuid.uuid4())[:8]
        self.output= output or self.createOutput(pollID=pollID,option=option)
        self.input = input or self.createInput(wallet=senderWallet,output=self.output)
    
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
    def fromJson(transactionJson):
        
        return Transaction(
            transactionID=transactionJson['transactionID'],
            output=transactionJson['output'],
            input=transactionJson['input']
        )


    @staticmethod
    def isValidTransaction(transaction):
        '''
        validates and raises an exception if invalid.
        '''

        if not Wallet.verify(transaction.input['publicKey'], transaction.output, transaction.input['signature']):
            raise Exception('Invalid signature')

def main():
    transaction= Transaction(Wallet(),'receip','1')
    transactionJson= transaction.toJson()
    restoredTransaction= transaction.fromJson(transactionJson)
    print(restoredTransaction.__dict__)
if __name__ == '__main__':
    main()