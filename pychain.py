# PyChain Ledger
################################################################################
# This module file contains the class definitions for 
# an app that builds a ledger using the `blockchain` approach

################################################################################
# Imports
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import hashlib

################################################################################
# Step 1:
# Create a Record Data Class

# Create a Record Data Class that consists of the `sender`, `receiver`, and
# `amount` attributes
@dataclass
class Record:
    """Record to store the sender, receiver and amount"""
    sender: str
    receiver: str
    amount: float

@dataclass
class Block:
    """Basic `block` structure to store the record, creator, previous hash and nonce puzzle"""
    record: Record
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    def hash_block(self):
        """Construct a 64-byte one-way hash using 256-bit SHA encoding"""
        sha = hashlib.sha256()

        record = str(self.record).encode()
        sha.update(record)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()


@dataclass
class PyChain:
    """PyChain class responsible for managing the build and validation of the blockchain"""
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):
        """Solves the nonce puzzle based on a difficuly level 
        - used to select a miner to add to the pychain"""
        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        return block

    def add_block(self, candidate_block):
        """Adds a candidate block to the pychain"""
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    def is_valid(self):
        """Validates the pychain integrity"""
        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                return False

            block_hash = block.hash_block()

        return True


