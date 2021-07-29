import hashlib
from datetime import datetime

class Block:

    # prev_hash = previous hash
    # trans_list = transaction list
    def __init__(self, prev_hash, data):
        self.prev_hash = prev_hash
        self.block_data = prev_hash + " - " + str(data)
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()