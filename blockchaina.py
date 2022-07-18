import hashlib

class CoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

if __name__ == "__main__":
    t1 = "Noah sends 5 C to Mark"
    t2 = "Mark sends 2.3 C to James"
    t3 = "James sends 4.2 C to Alisson"
    t4 = "Alisson sends 1.1 C to Noah"

    block1 = CoinBlock('firstblock', [t1, t2])

    print(f"Block 1 data: {block1.block_data}")
    print(f"Block 1 hash: {block1.block_hash}")

    block2 = CoinBlock(block1.block_hash, [t3, t4])

    print(f"Block 2 data: {block2.block_data}")
    print(f"Block 2 hash: {block2.block_hash}")