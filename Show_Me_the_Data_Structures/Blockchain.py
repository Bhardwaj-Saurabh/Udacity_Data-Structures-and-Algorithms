import hashlib
import datetime

def calc_hash(data, timestamp):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8') + str(timestamp).encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now(datetime.timezone.utc)  # UTC timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash(str(data), self.timestamp)
        self.prev = None  # Previous block

    def __repr__(self):
        return (
            f"Block Data: {repr(self.data)}\n"
            f"Hash: {repr(self.hash)}\n"
            f"Previous Hash: {repr(self.previous_hash)}\n"
            f"Timestamp: {repr(self.timestamp)}\n"
        )

class BlockChain:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Block(data, 0)
        else:
            new_block = Block(data, self.head.hash)
            new_block.prev = self.head
            self.head = new_block

    def size(self):
        size = 0
        temp = self.head
        while temp:
            size += 1
            temp = temp.prev
        return size

    def to_list(self):
        out = []
        block = self.head
        while block:
            out.append(block)
            block = block.prev
        return out

# Testing code
def test_blockchain():
    blockchain = BlockChain()
    blockchain.append("Genesis")
    blockchain.append("Exodus")
    blockchain.append("Leviticus")

    assert blockchain.size() == 3, "Test Failed: Blockchain should have 3 blocks"
    blocks = blockchain.to_list()
    assert blocks[0].data == "Leviticus", "Test Failed: Latest block should be 'Leviticus'"
    assert blocks[1].data == "Exodus", "Test Failed: Second block should be 'Exodus'"
    assert blocks[2].data == "Genesis", "Test Failed: First block should be 'Genesis'"

    print("All tests passed.")

test_blockchain()