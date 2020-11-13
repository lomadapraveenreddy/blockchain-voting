import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from blockchain.block import Block
from wallet.transaction import Transaction

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-8ef44544-2324-11eb-af2a-72ba4a3d8762'
pnconfig.publish_key = 'pub-c-1924a428-4020-47da-b9c8-5010d4f41049'
TEST_CHANNEL = 'TEST_CHANNEL'

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK',
    'TRANSACTION': 'TRANSACTION'
}


class Listener(SubscribeCallback):

    def __init__(self, blockchain,transactionPool):
        self.blockchain = blockchain
        self.transactionPool = transactionPool

    def message(self, pubnub, messageObj):
        #print(f'\nChannel:{messageObj.channel}|Message:{messageObj.message}')

        if messageObj.channel == CHANNELS['BLOCK']:
            receivedBlock = Block.fromJson(messageObj.message)
            newPotentialChain = self.blockchain.ledger[:]
            newPotentialChain.append(receivedBlock)
            try:
                self.blockchain.replaceLedger(newPotentialChain)
                self.transactionPool.clearTransactionPool(self.blockchain.ledger)
            except Exception as e:
                print(f'\n-- Did not replace old ledger {e}.')
        elif messageObj.channel==CHANNELS['TRANSACTION']:
            receivedTransaction = Transaction.fromJson(messageObj.message)
            if receivedTransaction.transactionID not in self.transactionPool.transactionMap.keys():
                self.transactionPool.setTransaction(receivedTransaction)
            print(f'\n-- Received transaction is set in transaction pool.')



class PubSub():
    '''
    Provides communication between nodes.
    '''

    def __init__(self, blockchain,transactionPool):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain,transactionPool))

    def publishMessage(self, channel, message):
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcastBlock(self, block):
        self.publishMessage(CHANNELS['BLOCK'], block.toJson())
    
    def broadcastTransaction(self, transaction):
        self.publishMessage(CHANNELS['TRANSACTION'], transaction.toJson())


def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publishMessage(TEST_CHANNEL, {'foo': 'bar'})


if __name__ == '__main__':
    main()
