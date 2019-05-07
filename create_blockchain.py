from blockchain import Blockchain


def create_blockchain(number_of_blocks):

    my_blockchain = Blockchain("Genesis Block")

    # Add blocks to the chain
    for i in xrange(1, number_of_blocks):
        my_blockchain.add_block("Block number " + str(i))

if __name__ == '__main__':
    create_blockchain(5)
