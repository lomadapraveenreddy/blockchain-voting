class TransactionPool:

    def __init__(self):
        self.transactionMap = {}

    def setTransaction(self, transaction):
        self.transactionMap[transaction.transactionID]=transaction

    def existingTransaction(self,address):

        for transaction in self.transactionMap.values():
            if address == transaction.input['senderAddress']:
                return transaction


    def clearTransactionPool(self,ledger):

        for block in ledger:
            for transaction in block.data:
                try:
                    del self.transactionMap[transaction['transactionID']]
                except KeyError:
                    pass