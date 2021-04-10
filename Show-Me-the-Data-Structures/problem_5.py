import hashlib
from datetime import datetime

class BlockChain:

    def __init__(self):
        self.tail = None

    def append(self, data):
        if not data:
            print("Error: empty data cannot be appended")
            return

        if self.tail == None:
            block = Block(datetime.utcnow(), data, None)
        else:
            block = Block(datetime.utcnow(), data, self.tail)

        self.tail = block

    def print(self):
        tail = self.tail
        if tail == None:
            print("No data")
        else:
            while tail:
                s = str(tail.timestamp) + " " + str(tail.data) + " " + str(tail.hash)
                print(s)
                tail = tail.previous_hash

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str_time = str(self.timestamp).encode('utf-8')
        hash_str_data = str(self.data).encode('utf-8')
        hash_str_prevhash = str(self.previous_hash).encode('utf-8')

        hash_str = hash_str_time + hash_str_data + hash_str_prevhash

        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return f'Block ID: {self.hash}'

print("\n---- TEST 1: No data ----")
bc = BlockChain()
bc.print()
# No data

print("\n---- TEST 2: Append empty data ----")
bc.append("")
bc.print()
# Error: empty data cannot be appended
# Nodata

print("\n---- TEST 3: Append data ----")
bc.append("First data")
bc.append("Second data")
bc.append("Third data")
bc.print()
# Three data should be output
