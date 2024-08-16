from hashlib import sha256
from cs50 import SQL


class Block:
    # initialising contents of block
    def __init__(
        self, file_name, data, reciever, index=1, nounce=0, prev_hash="0" * 64
    ):
        self.file_name = file_name
        self.data = data
        self.reciever = reciever
        self.nounce = nounce
        self.index = index
        self.prev_hash = prev_hash
        self.hash = self.generate_hash()

    # generate hash for the block
    def generate_hash(self):
        temp_hash = (
            str(self.nounce)
            + str(self.file_name)
            + str(self.data)
            + str(self.reciever)
            + str(self.prev_hash)
            + str(self.index)
        )
        self.hash = sha256(temp_hash.encode()).hexdigest()
        return self.hash

    # return string for printing the contents of block
    def __str__(self):
        return f"\nhash: {self.hash}\nprev_hash: {self.prev_hash}\nreciever: {self.reciever}\nfile_name: {self.file_name}\nnounce: {self.nounce}\nindex: {self.index}"


class Blockchain:
    # difficulty of the hash while mining
    difficulty = 2

    # loads the chain if given
    def __init__(self, chain=[]):
        self.chain = chain

    # add blocks to the chain
    def add_block(self, block):
        self.chain.append(block)

    # checks if the blocks in the blockchain is valid or not
    def is_valid(self):
        chain = self.chain
        diff = self.difficulty
        for i in range(0, len(chain) - 1):
            if (
                chain[i + 1].prev_hash != chain[i].generate_hash()
                or chain[i].generate_hash()[:diff] != "0" * diff
            ):
                return False
        return True

    # mining blocks by generating hash with pattern
    def mine(self, block):
        try:
            block.prev_hash = self.chain[-1].hash
        except IndexError:
            pass
        block.index = len(self.chain) + 1
        while True:
            temp_hash = block.generate_hash()
            if temp_hash[: self.difficulty] == "0" * self.difficulty:
                self.add_block(block)
                return self.is_valid()
            else:
                block.nounce += 1
