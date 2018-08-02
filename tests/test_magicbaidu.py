import os
import sys
import random
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from MagicBaidu import MagicBaidu


class TestMagicBaidu(unittest.TestCase):
    """
    Test MagicBaidu class
    """

    def setUp(self):
        self.mb = MagicGoogle()

    def tearDown(self):
        self.mb = None

    def test_search_url(self):
        sleep = random.randint(2, 15)
        result = list(self.mb.search_url(query='python', num=1, pause=sleep))
        self.assertEqual(result[0], 'https://www.python.org/', 'test search_url fail')


if __name__ == '__main__':
    unittest.main()
