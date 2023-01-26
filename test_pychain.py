# PyChain Ledger unit testing script

# Imports
import unittest
import pychain

class TestPychain(unittest.TestCase):
    def setUp(self):
        self.genesis = pychain.Block("Genesis", 0)

    def test_block_can_be_created(self):
        # Uses the setUp block as data to validate
        self.assertEqual(self.genesis.record, "Genesis")
        self.assertEqual(self.genesis.creator_id, 0)
        self.assertEqual(self.genesis.prev_hash, "0")
        self.assertEqual(self.genesis.nonce, 0)
        self.assertIsNotNone(self.genesis.timestamp)

if __name__ == "__main__":
    unittest.main()
