# PyChain Ledger unit testing script

# Imports
import unittest
import pychain
import re

class TestPychain(unittest.TestCase):
    def setUp(self):
        """Test record with values required by each test case"""
        self.record = pychain.Record(
            "Unit Test",
            "Unit Tester",
            999
        )


    def test_block_can_be_created(self):
        """Check that a valid block can be created"""
        self.test_block = pychain.Block(
            self.record,
            0,
            "0"
        )
        self.assertEqual(self.test_block.record.sender, "Unit Test")
        self.assertEqual(self.test_block.record.receiver, "Unit Tester")
        self.assertEqual(self.test_block.record.amount, 999)
        self.assertEqual(self.test_block.creator_id, 0)
        self.assertEqual(self.test_block.prev_hash, "0")
        self.assertEqual(self.test_block.nonce, 0)
        self.assertIsNotNone(self.test_block.timestamp)


if __name__ == "__main__":
    unittest.main()
