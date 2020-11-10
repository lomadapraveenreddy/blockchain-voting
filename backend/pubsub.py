import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from blockchain.block import Block

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-8ef44544-2324-11eb-af2a-72ba4a3d8762'
pnconfig.publish_key = 'pub-c-1924a428-4020-47da-b9c8-5010d4f41049'
TEST_CHANNEL = 'TEST_CHANNEL'

CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}


class Listener(SubscribeCallback):

    def __init__(self, blockchain):
        self.blockchain = blockchain

    def message(self, pubnub, messageObj):
        #print(f'\nChannel:{messageObj.channel}|Message:{messageObj.message}')

        if messageObj.channel == CHANNELS['BLOCK']:
            receivedBlock = Block.fromJson(messageObj.message)
            newPotentialChain = self.blockchain.ledger[:]
            newPotentialChain.append(receivedBlock)
            try:
                self.blockchain.replaceLedger(newPotentialChain)
            except Exception as e:
                print(f'\n-- Did not replace old ledger {e}.')


class PubSub():
    '''
    Provides communication between nodes.
    '''

    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))

    def publishMessage(self, channel, message):
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcastBlock(self, block):
        self.publishMessage(CHANNELS['BLOCK'], block.toJson())


def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publishMessage(TEST_CHANNEL, {'foo': 'bar'})


if __name__ == '__main__':
    main()
