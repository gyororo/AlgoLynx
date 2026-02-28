# test_algolynx.py
"""
Tests for AlgoLynx module.
"""

import unittest
from algolynx import AlgoLynx

class TestAlgoLynx(unittest.TestCase):
    """Test cases for AlgoLynx class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AlgoLynx()
        self.assertIsInstance(instance, AlgoLynx)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AlgoLynx()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
