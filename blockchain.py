from itertools import count
from block import Block


class Blockchain(object):
    _indices = count(0)

    def __init__(self, genesis_block_data):
        self.__chain = []
        genesis_block = self.__create_genesis_block(genesis_block_data)
        self.__chain.append(genesis_block)

    @property
    def last_block(self):
        """
        Returns last block of blockchain
        """
        return self.__chain[-1]

    def __create_genesis_block(self, genesis_block_data):
        """
        Construct a block with previous hash as 0
        """
        genesis_block = Block(genesis_block_data, "0", next(self._indices))
        print "Adding Block {0} : {1} at {2}".format(
            genesis_block.index, genesis_block.hash, genesis_block.timestamp)
        return genesis_block

    def add_block(self, new_block_data):
        """
        Create Block object
        """
        new_block = Block(
            new_block_data,
            self.last_block.hash,
            next(self._indices)
        )
        print "Adding Block {0} : {1} at {2}".format(
            new_block.index, new_block.hash, new_block.timestamp)
        self.__chain.append(new_block)

    def get_chain(self):
        return self._chain

    def set_chain(self, value):
        if value:
            raise ValueError
        else:
            self._chain = value

    __chain = property(get_chain, set_chain)
