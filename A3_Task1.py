import hashlib
import datetime

# Block Class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()


# Blockchain Class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Pakistan Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()

        new_block = Block(
            len(self.chain),
            datetime.datetime.now(),
            data,
            previous_block.hash
        )

        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print("\n----------------------------")
            print("Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)


# Create Blockchain
blockchain = Blockchain()

# Transactions
blockchain.add_block("Ali from Islamabad sent 5000 to Ahmed in Lahore")
blockchain.add_block("Abiha from Karachi paid 2500 to Hina in Rawalpindi")
blockchain.add_block("Abdullah from Peshawar sent 7000 to Bilal in Attock")
blockchain.add_block("Fatima from Faisalabad paid 1500 to Abbas in Attock")

# Display Blockchain
print("\nOriginal Blockchain:")
blockchain.display_chain()

# Tampering Demonstration
print("\nTampering with Block 2...\n")

blockchain.chain[2].data = "Hacked Transaction in Karachi"
blockchain.chain[2].hash = blockchain.chain[2].calculate_hash()

# Display After Tampering
print("\nBlockchain After Tampering:")
blockchain.display_chain()