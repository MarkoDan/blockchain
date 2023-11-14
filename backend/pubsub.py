from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
# import threading
import time

from backend.blockchain.block import Block


publish_key = 'pub-c-9fbd0eff-b7c0-4e48-8eb5-b29bb8ea904f'
subscribe_key = 'sub-c-e732071d-60cc-4e82-b055-efa389b3cd9a'

pnconfig = PNConfiguration()
pnconfig.subscribe_key = subscribe_key
pnconfig.publish_key = publish_key
pnconfig.uuid = 'myUniqueClientId'
pubnub = PubNub(pnconfig)



CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}

class Listener(SubscribeCallback):
    
    def __init__(self, blockchain):
        self.blockchain = blockchain
    

    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print('\n -- Succesfully replace the local chain')
            except Exception as e:
                print(f'\n -- Did not replace chain: {e}')
class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))


    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.unsubscribe().channels([channel]).execute()
        self.pubnub.publish().channel(channel).message(message).sync()
        self.pubnub.subscribe().channels([channel]).execute()

    def broadcast_block(self, block):
        """
        Broadcast a block object to all nodes
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())

# def publish_message():
#     pubnub.publish().channel(TEST_CHANNEL).message({'foo': 'bar'}).sync()


def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(CHANNELS['TEST'], { 'foo': 'bar' })

if __name__ == '__main__':
    main()
