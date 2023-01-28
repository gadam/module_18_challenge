# PyChain Ledger unit testing script

# Imports
import unittest
import pychain
import hashlib
import re

class TestPychain(unittest.TestCase):
    def setUp(self):
        """Test record with values required by each test case"""
        self.record = pychain.Record(
            "Unit Test",
            "Unit Tester",
            999
        )

        self.test_block = pychain.Block(
            self.record,
            0,
            "0"
        )

    def test_block_can_be_created(self):
        """Check that a valid block can be created"""
        self.assertEqual(self.test_block.record.sender, "Unit Test")
        self.assertEqual(self.test_block.record.receiver, "Unit Tester")
        self.assertEqual(self.test_block.record.amount, 999)
        self.assertEqual(self.test_block.creator_id, 0)
        self.assertEqual(self.test_block.prev_hash, "0")
        self.assertEqual(self.test_block.nonce, 0)
        self.assertIsNotNone(self.test_block.timestamp)

    def test_block_can_be_hashed(self):
        """Check that block is correctly hashed using SHA256"""
        sha_pattern = "^[a-fA-F0-9]{64}$"
        self.assertTrue(
            re.match(
                sha_pattern, 
                self.test_block.hash_block()
            )
        )

    def test_proof_of_work_finds_nonce(self):
        """Check that the Proof of Work validation finds the correct code"""
        blockchain = pychain.PyChain([self.test_block])
        block = blockchain.proof_of_work(blockchain.chain[0])
        self.assertIsNot(block.nonce, 0)

    def test_block_added_to_chain(self):
        """Check that a block can be added to the chain"""
        blockchain = pychain.PyChain([self.test_block])
        prev_block_hash = self.test_block.hash_block()
        record = pychain.Record(
            "Add Block",
            "Unit Tester",
            888
        )
        new_block = pychain.Block(
            record,
            1,
            prev_block_hash
        )
        blockchain.add_block(new_block)
        self.assertEqual(len(blockchain.chain), 2)
        
    def test_adding_new_blocks_maintains_valid_chain(self):
        """Check that a block added to the chain maintains chain integrity"""
        blockchain = pychain.PyChain([self.test_block])
        prev_block_hash = self.test_block.hash_block()
        record = pychain.Record(
            "Add Block",
            "Unit Tester",
            888
        )
        new_block = pychain.Block(
            record,
            1,
            prev_block_hash
        )
        blockchain.add_block(new_block)    
        self.assertTrue(blockchain.is_valid())
        
    def test_adding_invalid_block_can_be_detected(self):
        """Check that an invalid block added to the chain can be detected"""
        blockchain = pychain.PyChain([self.test_block])
        sha = hashlib.sha256()
        sha.update(str("Random string").encode())
        record = pychain.Record(
            "Add Invalid Block",
            "Unit Tester",
            777
        )
        new_block = pychain.Block(
            record,
            1,
            sha.hexdigest()
        )
        blockchain.add_block(new_block)    
        self.assertFalse(blockchain.is_valid())

if __name__ == "__main__":
    unittest.main()
