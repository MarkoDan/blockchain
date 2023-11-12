from backend.blockchain.block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    
    def add_block(self, data):
        last_block = self.chain[-1]
        block = Block.mine_block(last_block, data)
        self.chain.append(block)

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain.
         - the chain must start with the genesis block
         - block must be formatted correctly
        """
        first_block = chain[0]
        if first_block != Block.genesis():
            raise Exception('The genesis block must be valid')
        
        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i - 1]
            Block.is_valid_block(last_block, block)



def main():

    blockchain = Blockchain()

    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)



if __name__ == '__main__':
    main()