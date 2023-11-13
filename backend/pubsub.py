from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
import threading

publish_key = 'pub-c-9fbd0eff-b7c0-4e48-8eb5-b29bb8ea904f'
subscribe_key = 'sub-c-e732071d-60cc-4e82-b055-efa389b3cd9a'

pnconfig = PNConfiguration()
pnconfig.subscribe_key = subscribe_key
pnconfig.publish_key = publish_key
pnconfig.uuid = 'myUniqueClientId'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')

pubnub.add_listener(Listener())
pubnub.subscribe().channels([TEST_CHANNEL]).execute()

def publish_message():
    pubnub.publish().channel(TEST_CHANNEL).message({'foo': 'bar'}).sync()

def main():
    publisher_thread = threading.Thread(target=publish_message)
    publisher_thread.start()
    publisher_thread.join()

if __name__ == '__main__':
    main()
