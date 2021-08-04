import random
import hashlib
import time

class PoW:

    def __init__(self, cpus, block):

        # Equivalente = 1 0's al frente de hash
        self.difficulty_hash = 0x0FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

        self.miners = []
        for cpu in cpus:
            self.miners.extend(cpu)
        random.shuffle(self.miners)

        while int(block.block_hash, 16) >= self.difficulty_hash:
            block.nonce += 1
            block.block_hash = hashlib.sha256(block.block_hash.encode()).hexdigest()
            # print('Resultant Hash: ' + str(block.block_hash))
            # print('Decimal value of hash: ' + str(int(block.block_hash, 16)) + '\n')
            miner = self.miners[block.nonce % len(self.miners)]

        print('\n\nNonce Guess: ' + str(block.nonce))
        print('Valid hash: ' + str(int(block.block_hash, 16)) + ' is less than ' + str(self.difficulty_hash))
        print('Miner: '+miner)
